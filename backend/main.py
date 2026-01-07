import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import OrderCreate
from database import MENU_DB, ORDERS_DB, next_order_id

app = FastAPI(title="Pizza Ordering Backend")

# Configure CORS to allow frontend access (especially important for local testing/Vercel deployment)
# In production, origins should be restricted, but we use * for broad deployment compatibility.
origins = [
    "http://127.0.0.1:5500",  # Local frontend server
    "*" # Allow all for deployment simplicity
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

@app.get("/api/v1/pizzas")
def get_pizzas():
    """Returns the current pizza menu."""
    return MENU_DB

@app.post("/api/v1/orders")
def create_order(order: OrderCreate):
    """Receives a new order, validates items, and stores it in memory."""
    global next_order_id
    
    order_total = 0.0
    
    # 1. Validate items against the menu
    for item in order.items:
        menu_item = next((p for p in MENU_DB if p["id"] == item.pizza_id), None)
        if not menu_item:
            raise HTTPException(status_code=400, detail=f"Pizza ID {item.pizza_id} not found in menu.")
        
        if item.quantity <= 0:
            raise HTTPException(status_code=400, detail="Order quantity must be positive.")
            
        order_total += menu_item["price"] * item.quantity

    # 2. Store Order
    new_order = {
        "order_id": next_order_id,
        "customer_info": order.customer_info.dict(),
        "items": [item.dict() for item in order.items],
        "total": round(order_total, 2),
        "status": "Received"
    }
    
    ORDERS_DB.append(new_order)
    next_order_id += 1
    
    return {
        "order_id": new_order["order_id"],
        "status": new_order["status"],
        "total": new_order["total"]
    }

# Optional: Endpoint to check orders (useful for debugging/testing)
@app.get("/api/v1/orders")
def get_orders():
    return ORDERS_DB

# Health check for deployment readiness
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "pizza-backend"}