import json
import os
from jsonschema import validate, ValidationError


def load_schema(schema_name: str) -> dict:
    """Load JSON schema from a file"""
    schema_dir = os.path.join(os.path.dirname(__file__), "..", "schemas")
    schema_path = os.path.join(schema_dir, schema_name)

    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file '{schema_name}' not found in {schema_dir}")

    with open(schema_path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_json_schema(json_data: dict, schema_name: str):
    """JSON validation with schema"""
    schema = load_schema(schema_name)
    try:
        validate(instance=json_data, schema=schema)
        return True
    except ValidationError as e:
        raise AssertionError(f"Schema validation failed: {e.message}")
