import pytest
from fastapi import HTTPException
from app.main import (
    get_products,
    get_product,
    create_product,
    delete_product,
    Product,
    ProductCreate,
    db,
)


def test_create_product_function():
    initial_len = len(db)
    prod = ProductCreate(title="Bolsa", price=200)
    new_prod = create_product(prod)

    assert new_prod.title == "Bolsa"
    assert new_prod.price == 200
    assert len(db) == initial_len + 1

    # cleanup
    db.remove(new_prod)


def test_get_products_returns_list():
    products = get_products()
    assert isinstance(products, list)
    assert all(isinstance(p, Product) for p in products)


def test_get_product_valid():
    prod = get_product(1)
    assert prod.title == "Camisa"
    assert prod.price == 50


def test_get_product_invalid():
    with pytest.raises(HTTPException) as exc:
        get_product(999)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Product not found"


def test_create_product_increments_id():
    initial_len = len(db)
    prod = ProductCreate(title="Sapato", price=300)
    new_prod = create_product(prod)

    assert new_prod.id == initial_len + 1
    assert new_prod in db

    # cleanup
    db.remove(new_prod)


def test_delete_product_valid():
    prod = ProductCreate(title="Cinto", price=80)
    new_prod = create_product(prod)

    response = delete_product(new_prod.id)
    assert response == {"message": "Deleted"}
    assert new_prod not in db


def test_delete_product_invalid():
    with pytest.raises(HTTPException) as exc:
        delete_product(999)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Not found"
