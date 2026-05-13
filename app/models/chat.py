from pydantic import BaseModel, Field
from typing import List, Optional, Literal

# 1. Standard Chat Models (For Web Chat Widget / API Clients)

class Message(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str
    name: Optional[str] = None

class ChatRequest(BaseModel):
    identifier: str = Field(
        ..., 
        description="The user's phone number or web session ID",
        example="+13035551234"
    )
    messages: List[Message] = Field(
        ..., 
        description="The conversation history."
    )

class ChatResponse(BaseModel):
    response: str = Field(
        ..., 
        description="The AI's natural language reply"
    )

# 2. Twilio SMS Webhook Model 
# Twilio does NOT send JSON. It sends application/x-www-form-urlencoded.

class TwilioSMSRequest(BaseModel):
    MessageSid: str
    SmsSid: str
    AccountSid: str
    MessagingServiceSid: Optional[str] = None
    From: str  # The customer/worker's phone number
    To: str    # Your Twilio phone number
    Body: str  # The actual text message sent by the user
    NumMedia: int = 0