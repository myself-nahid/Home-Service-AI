import httpx
from app.core.config import settings

async def fetch_user_context(identifier: str) -> dict:
    """
    MOCKED for local testing. Identifies the 4 distinct roles.
    """
    # 1. CLEANER
    if identifier == "+1_cleaner":
        return {
            "role": "cleaner", 
            "name": "John (Cleaner)", 
            "current_job": "742 Evergreen Terrace (10:00 AM - 1:45 PM)"
        }
    
    # 2. MANAGER (Property Manager / B2B)
    elif identifier == "+1_manager":
        return {
            "role": "manager",
            "name": "Derek M.",
            "managed_properties": 3,
            "business_name": "Denver STR Hosting"
        }
        
    # 3. ADMIN (Operations / Dispatcher)
    elif identifier == "+1_admin":
        return {
            "role": "admin",
            "name": "Sarah (Ops)",
            "access_level": "super_admin"
        }
    
    # 4. CUSTOMER (Default fallback)
    return {
        "role": "customer", 
        "name": "Jane Smith", 
        "active_jobs": "None"
    }

async def trigger_backend_action(service_url: str, endpoint: str, payload: dict) -> dict:
    """
    We will ignore this function for now since we are going to 
    mock the tool executors in the next file.
    """
    pass