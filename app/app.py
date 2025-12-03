from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Store API")


class Product(BaseModel):
    id: int
    title: str
    price: float


class ProductCreate(BaseModel):
    title: str
    price: float


# Simulated "database"
db: list[Product] = [
    Product(id=1, title="Camisa", price=50),
    Product(id=2, title="Calça", price=120),
]


@app.get("/products")
def get_products():
    return db


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for p in db:
        if p.id == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", response_model=Product)
def create_product(prod: ProductCreate):
    new_id = max((p.id for p in db), default=0) + 1
    new_prod = Product(id=new_id, **prod.dict())
    db.append(new_prod)
    return new_prod


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for p in db:
        if p.id == product_id:
            db.remove(p)
            return {"message": "Deleted"}

    raise HTTPException(status_code=404, detail="Not found")
