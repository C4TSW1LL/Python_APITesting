def jsonplaceholder_schema(request_type):
    if request_type == "posts":
        schema = {
            "type": "object",
            "properties": {
                "userId": {"type": "integer"},
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "body": {"type": "string"}
            },
            "required": ["userId", "id", "title", "body"]}
    if request_type == "comments":
        schema = {
            "type": "object",
            "properties": {
                "postId": {"type": "integer"},
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "email": {"type": "string"},
                "body": {"type": "string"}
            },
            "required": ["postId", "id", "name", "email", "body"]}

    if request_type == 'photos':
        schema = {
            "type": "object",
            "properties": {
                "albumId": {"type": "integer"},
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "url": {"type": "string", "format": "uri", "qt-uri-protocols": ["https"]},
                "thumbnailUrl": {"type": "string", "format": "uri", "qt-uri-protocols": ["https"]}},
            "required": ["albumId", "id", "thumbnailUrl", "title", "url"]}
    if request_type == 'empty':
            schema = {}
    return schema
