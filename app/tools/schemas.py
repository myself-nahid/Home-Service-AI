TOOLS_BY_ROLE = {
    # 1. CUSTOMER TOOLS
    "customer":[
        {
            "type": "function",
            "function": {
                "name": "calculate_quote",
                "description": "Calculates quote price based on home size.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bedrooms": {"type": "integer"},
                        "bathrooms": {"type": "number"},
                        "add_ons": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["bedrooms", "bathrooms"]
                }
            }
        }
    ],
    
    # 2. CLEANER TOOLS
    "cleaner":[
        {
            "type": "function",
            "function": {
                "name": "request_time_extension",
                "description": "Requests extra time for the current job from the customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "extra_minutes": {"type": "integer"},
                        "reason": {"type": "string"}
                    },
                    "required": ["extra_minutes", "reason"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_daily_schedule",
                "description": "Fetches the cleaner's jobs for the day."
            }
        }
    ],
    
    # 3. MANAGER TOOLS
    "manager":[
        {
            "type": "function",
            "function": {
                "name": "request_property_setup",
                "description": "Initiates the onboarding process for a new property to be managed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "address": {"type": "string"}
                    },
                    "required": ["address"]
                }
            }
        }
    ],
    
    # 4. ADMIN TOOLS
    "admin":[
        {
            "type": "function",
            "function": {
                "name": "reassign_cleaner",
                "description": "Forces a reassignment of a job to a different cleaner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {"type": "string"},
                        "new_cleaner_id": {"type": "string"}
                    },
                    "required": ["job_id", "new_cleaner_id"]
                }
            }
        }
    ]
}