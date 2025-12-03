import requests
from .conftest import BASE_URL, validate_schema


product_schema = {
    "id": int,
    "title": str,
    "price": float,
}


def test_get_all_products():
    r = requests.get(f"{BASE_URL}/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

    # Validar contratos
    for p in r.json():
        validate_schema(p, product_schema)


def test_get_valid_product():
    r = requests.get(f"{BASE_URL}/products/1")
    assert r.status_code == 200
    validate_schema(r.json(), product_schema)


def test_get_invalid_product():
    r = requests.get(f"{BASE_URL}/products/999")
    assert r.status_code == 404


def test_create_product():
    payload = {"title": "Tenis", "price": 300}
    r = requests.post(f"{BASE_URL}/products", json=payload)

    assert r.status_code == 200
    body = r.json()

    validate_schema(body, product_schema)

    # cleanup
    requests.delete(f"{BASE_URL}/products/{body['id']}")


def test_missing_price():
    r = requests.post(f"{BASE_URL}/products", json={"title": "Cadeira"})
    assert r.status_code == 422


def test_missing_title():
    r = requests.post(f"{BASE_URL}/products", json={"price": 40})
    assert r.status_code == 422


def test_invalid_price_type():
    r = requests.post(f"{BASE_URL}/products", json={"title": "Mesa", "price": "caro"})
    assert r.status_code == 422


def test_invalid_route():
    r = requests.get(f"{BASE_URL}/wrong")
    assert r.status_code == 404
