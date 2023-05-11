def open_brewery_schema(request_type):
    if request_type == 'object':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "brewery_type": {
                    "type": "string"
                },
                "address_1": {
                    "type": "string"
                },
                "address_2": {
                    "type": "null"
                },
                "address_3": {
                    "type": "null"
                },
                "city": {
                    "type": "string"
                },
                "state_province": {
                    "type": "string"
                },
                "postal_code": {
                    "type": "string"
                },
                "country": {
                    "type": "string"
                },
                "longitude": {
                    "type": "string"
                },
                "latitude": {
                    "type": "string"
                },
                "phone": {
                    "type": "string"
                },
                "website_url": {
                    "type": "string"
                },
                "state": {
                    "type": "string"
                },
                "street": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "name",
                "brewery_type",
                "address_1",
                "address_2",
                "address_3",
                "city",
                "state_province",
                "postal_code",
                "country",
                "longitude",
                "latitude",
                "phone",
                "website_url",
                "state",
                "street"
            ]
        }
    if request_type == 'array':
        schema = {
            "properties": {
                "id": {
                    "type": "string"},
                "name": {
                    "type": "string"},
                "brewery_type": {
                    "type": "string"},
                "street": {
                    "type": ["string", "null"]},
                "address_2": {
                    "type": ["string", "null"]},
                "address_3": {
                    "type": ["string", "null"]},
                "city": {
                    "type": "string"},
                "state": {
                    "type": "string"},
                "county_province": {
                    "type": ["string", "null"]},
                "postal_code": {
                    "type": "string"},
                "country": {
                    "type": "string"},
                "longitude": {
                    "type": ["string", "null"]},
                "latitude": {
                    "type": ["string", "null"]},
                "phone": {
                    "type": ["string", "null"]},
                "website_url": {
                    "type": ["string", "null"],
                    "format": "uri",
                    "qt-uri-protocols": [
                        "http"]},
                "updated_at": {
                    "type": "string",
                    "format": "date-time"},
                "created_at": {
                    "type": "string",
                    "format": "date-time"}},
            "required": [
                "address_2",
                "address_3",
                "brewery_type",
                "city",
                "country",
                "county_province",
                "created_at",
                "id",
                "latitude",
                "longitude",
                "name",
                "phone",
                "postal_code",
                "state",
                "street",
                "updated_at",
                "website_url"
            ],
        }
    if request_type == 'empty':
        schema = {
            "type": "array",
            "items": {},
            "definitions": {}
        }

    return schema
