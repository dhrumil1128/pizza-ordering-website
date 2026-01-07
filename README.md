# Pizza Ordering Website

This repository contains a full-stack pizza ordering application featuring a Bootstrap frontend and a FastAPI backend.

## Project Structure

```
/pizza-ordering-app
├── backend/
│   ├── main.py             (FastAPI application logic)
│   ├── models.py           (Pydantic schemas)
│   ├── database.py         (Mock data storage)
│   └── requirements.txt    (Python dependencies)
│
└── frontend/
    └── index.html          (Main HTML structure, Bootstrap integration)
```

## Environment Variables

For local development, the frontend assumes the backend runs on `http://127.0.0.1:8000`.

| Variable Name | Required For | Location | Notes |
| :--- | :--- | :--- | :--- |
| `PORT` | Backend (Deployment) | Render/System Env | Required for deployment platforms (e.g., Render) to bind the Uvicorn server correctly. |

## API Integration Notes

The frontend communicates with the backend on port 8000 using the `/api/v1/` prefix.

*   **Menu Fetch:** Frontend performs a `GET` request to `/api/v1/pizzas`.
*   **Order Placement:** Frontend performs a `POST` request to `/api/v1/orders`.

## How To Run Locally

### Step 1: Setup Backend (FastAPI)

1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```
2.  Create and activate a Python virtual environment (Recommended).
3.  Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Start the FastAPI server using Uvicorn:
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

### Step 2: Setup Frontend (Static Server)

1.  Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```
2.  Serve the static files using Python's built-in server:
    ```bash
    python -m http.server 5500
    ```

### Step 3: Access the Application

Open your browser and navigate to `http://127.0.0.1:5500`.

## Deployment Notes (Vercel/Render)

*   **Frontend (Vercel):** Deploy the `frontend` directory directly. Vercel will serve `frontend/index.html` statically.
*   **Backend (Render):** Deploy the `backend` directory using a Web Service container, ensuring the startup command uses Uvicorn targeting `$PORT`, e.g., `uvicorn main:app --host 0.0.0.0 --port $PORT`.