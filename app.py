from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Store API")

class Product(BaseModel):
    id: int
    title: str
    price: float

# Banco fake (em memória)
db = [
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
    raise HTTPException(404, "Product not found")

@app.post("/products")
def create_product(prod: Product):
    # Valida duplicado
    for p in db:
        if p.id == prod.id:
            raise HTTPException(400, "ID duplicado")
    db.append(prod)
    return prod

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for p in db:
        if p.id == product_id:
            db.remove(p)
            return {"message": "Deleted"}
    raise HTTPException(404, "Not found")
