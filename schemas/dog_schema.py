def dog_schema(msg_type):
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": msg_type},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    return schema