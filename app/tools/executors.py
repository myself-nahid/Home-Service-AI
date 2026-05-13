from app.clients.backend_client import trigger_backend_action
from app.core.config import settings

async def execute_tool(tool_name: str, arguments: dict) -> str:
    if tool_name == "calculate_quote":
        # Calls the Pricing Microservice
        res = await trigger_backend_action(settings.PRICING_SERVICE_URL, "api/pricing/calculate", arguments)
        return f"Quote generated: Max price is ${res['total_price']} for {res['estimated_hours']} hours."
    
    elif tool_name == "request_time_extension":
        # Calls the CRM microservice to pause the job and text the customer
        res = await trigger_backend_action(settings.CRM_SERVICE_URL, "api/jobs/extend", arguments)
        return "Extension requested. The customer has been texted for approval. I will notify you when they reply."
    
    return "Tool not found."