from fastapi import APIRouter, HTTPException, Form, Depends
from app.models.chat import ChatRequest, ChatResponse, TwilioSMSRequest
from app.clients.backend_client import fetch_user_context
from app.services.ai_orchestrator import handle_chat

router = APIRouter()

# ENDPOINT 1: Web Chat Widget (Standard JSON)
@router.post("/chat", response_model=ChatResponse)
async def web_chat_endpoint(req: ChatRequest):
    try:
        # 1. Fetch user role/context from User Microservice
        context = await fetch_user_context(req.identifier)
        
        # Convert Pydantic models to dicts for OpenAI
        message_history = [msg.model_dump(exclude_none=True) for msg in req.messages]
        
        # 2. Process with AI Orchestrator
        ai_reply = await handle_chat(req.identifier, context, message_history)
        
        return ChatResponse(response=ai_reply)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ENDPOINT 2: Twilio SMS Webhook (Form Data)
@router.post("/twilio/webhook")
async def twilio_sms_endpoint(
    From: str = Form(...),
    Body: str = Form(...)
):
    """
    Twilio sends data as form fields, not JSON. FastAPI's `Form(...)` 
    catches this perfectly.
    """
    try:
        identifier = From # e.g., "+13035551234"
        
        # 1. Fetch context based on phone number
        context = await fetch_user_context(identifier)
        
        # 2. In a stateless microservice, you need to fetch the chat history 
        # for this phone number from your DB/CRM microservice here.
        # For example: 
        # message_history = await fetch_chat_history(identifier)
        
        # For now, we'll assume a fresh array with just the incoming text:
        message_history = [{"role": "user", "content": Body}]
        
        # 3. Process with AI Orchestrator
        ai_reply = await handle_chat(identifier, context, message_history)
        
        # 4. Return TwiML (XML) response back to Twilio so it texts the user back
        # Note: In FastAPI, you can return a Response object with media_type="application/xml"
        from fastapi import Response
        twiml_response = f"""
        <Response>
            <Message>{ai_reply}</Message>
        </Response>
        """
        return Response(content=twiml_response, media_type="application/xml")
        
    except Exception as e:
        # If the AI fails, send a safe fallback SMS so the user isn't left hanging
        fallback_twiml = """
        <Response>
            <Message>Sorry, I'm having trouble connecting right now. A human team member will text you shortly.</Message>
        </Response>
        """
        return Response(content=fallback_twiml, media_type="application/xml")