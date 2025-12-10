import requests
from tests.conftest import BASE_URL, validate_schema


product_schema = {
    "id": int,
    "title": str,
    "price": float,
}


def test_end_to_end():
    # Create
    payload = {"title": "Notebook", "price": 4000}
    r = requests.post(f"{BASE_URL}/products", json=payload)
    assert r.status_code == 200
    body = r.json()
    validate_schema(body, product_schema)

    prod_id = body["id"]

    # Retrieve
    r = requests.get(f"{BASE_URL}/products/{prod_id}")
    assert r.status_code == 200
    validate_schema(r.json(), product_schema)

    # Validate in listing
    r = requests.get(f"{BASE_URL}/products")
    assert any(p["id"] == prod_id for p in r.json())

    # Delete
    r = requests.delete(f"{BASE_URL}/products/{prod_id}")
    assert r.status_code == 200

    # Validate deleted
    r = requests.get(f"{BASE_URL}/products/{prod_id}")
    assert r.status_code == 404
