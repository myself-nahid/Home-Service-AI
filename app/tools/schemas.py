TOOLS_BY_ROLE = {
    "residential_customer":[
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
    "worker":[
        {
            "type": "function",
            "function": {
                "name": "request_time_extension",
                "description": "Requests extra time for the current job from the customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {"type": "string"},
                        "extra_minutes": {"type": "integer"}
                    },
                    "required": ["job_id", "extra_minutes"]
                }
            }
        }
    ]
}
