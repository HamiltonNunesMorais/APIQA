import requests

BASE_URL = "http://localhost:8000"

def test_get_all_products():
    r = requests.get(f"{BASE_URL}/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_get_valid_product():
    r = requests.get(f"{BASE_URL}/products/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_get_invalid_product():
    r = requests.get(f"{BASE_URL}/products/999")
    assert r.status_code == 404

def test_create_product():
    payload = {
        "title": "Tenis",
        "price": 300
    }
    r = requests.post(f"{BASE_URL}/products", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == "Tenis"
    assert body["price"] == 300
