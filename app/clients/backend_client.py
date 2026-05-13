import httpx
from app.core.config import settings

async def fetch_user_context(identifier: str) -> dict:
    """Fetches user role and context from the User Microservice."""
    async with httpx.AsyncClient() as client:
        # Example: GET http://user-service/api/users/context?id=+13035551234
        response = await client.get(f"{settings.USER_SERVICE_URL}/api/users/context", params={"id": identifier})
        if response.status_code == 200:
            return response.json()
        # Default fallback for new users
        return {"role": "residential_customer", "name": "Guest", "history":[]}

async def trigger_backend_action(service_url: str, endpoint: str, payload: dict) -> dict:
    """Generic tool executor that POSTs to other microservices."""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{service_url}/{endpoint}", json=payload)
        return response.json()