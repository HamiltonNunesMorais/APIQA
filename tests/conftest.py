import pytest
import requests

BASE_URL = "http://localhost:8000"

@pytest.fixture
def create_product():
    """Fixture para criar e limpar produto automaticamente."""
    payload = {"title": "mock-product", "price": 10}
    r = requests.post(f"{BASE_URL}/products", json=payload)
    assert r.status_code == 200
    prod_id = r.json()["id"]
    
    yield prod_id
    
    # cleanup
    requests.delete(f"{BASE_URL}/products/{prod_id}")


def validate_schema(data, schema):
    """Valida contrato simples (como no Postman)."""
    for key, expected_type in schema.items():
        assert key in data, f"Missing field '{key}'"
        assert isinstance(data[key], expected_type), f"{key} has wrong type"
