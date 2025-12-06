from fastapi import FastAPI
from models import Products
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


products = [
        Products(id=1,name="asus",desc="casual use",quant=10),
        Products(id=2,name="HP",desc="Gaming",quant=6),
    ]

@app.get("/products")
def all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
        
    return "Product Not Found"


@app.post("/product")
def add_product(product : Products):
    products.append(product)
    return product