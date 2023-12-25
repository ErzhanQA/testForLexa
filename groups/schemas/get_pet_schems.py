get_pet_schemas = {
    200: {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "category":
                {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
            "name": {"type": "string"},
            "photoUrls": [{"type": "string"}],
            "tags": [
                {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                }
            ],
            "status": {"type": "string"},
        },
        "required": ["name", "photoUrls"]
    },
    404: {
        "type": "object",
        "properties": {
            "code": {"type": "integer"},
            "type": {"type": "string"},
            "message": {"type": "string"}
        }
    },
}
