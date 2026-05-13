import json
from openai import AsyncOpenAI
from app.core.config import settings
from app.prompts.roles import get_system_prompt
from app.tools.schemas import TOOLS_BY_ROLE
from app.tools.executors import execute_tool

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

async def handle_chat(user_id: str, context: dict, messages: list) -> str:
    role = context.get("role", "residential_customer")
    
    # 1. Inject Role-Specific System Prompt
    system_message = {"role": "system", "content": get_system_prompt(role, context)}
    conversation = [system_message] + messages

    # 2. Get Role-Specific Tools
    tools = TOOLS_BY_ROLE.get(role,[])

    # 3. Call OpenAI
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=conversation,
        tools=tools if tools else None,
        tool_choice="auto" if tools else None
    )
    
    response_message = response.choices[0].message

    # 4. Handle Tool Calls (If AI decides it needs to talk to a microservice)
    if response_message.tool_calls:
        conversation.append(response_message) # Append AI's intent to use a tool
        
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            # Execute HTTP call to other microservice
            tool_result = await execute_tool(function_name, arguments)
            
            # Append Microservice Result back to conversation
            conversation.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": str(tool_result)
            })
            
        # 5. Second LLM Call: Generate natural language response based on Microservice data
        final_response = await client.chat.completions.create(
            model="gpt-4o",
            messages=conversation
        )
        return final_response.choices[0].message.content

    # 6. Return standard text response if no tools were called
    return response_message.content