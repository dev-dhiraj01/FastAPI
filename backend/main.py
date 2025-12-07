from fastapi import  Depends , FastAPI
from models import Products
from database import session , engine 
import databases_models
from sqlalchemy.orm import Session

app = FastAPI()
databases_models.Base.metadata.create_all(bind = engine)
@app.get("/")
def read_root():
    db = session()
    db.query()
    return {"Hello": "World"}


products = [
        Products(id=1,name="asus",desc="casual use",price=200,quant=10),
        Products(id=2,name="HP",desc="Gaming",price=520,quant=6),
    ]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(databases_models.Products).count
    if count == 0:
        for product in products:
            db.add(databases_models.Products(**product.model_dump()))
        db.commit()

init_db()


@app.get("/products")
def all_products(db : Session = Depends(get_db)):
    db_products = db.query(databases_models.Products).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int,db : Session = Depends(get_db)):
    db_product = db.query(databases_models.Products).filter(databases_models.Products.id == id).first()
    if db_product:
        return db_product
        
    return "Product Not Found"


@app.post("/product")
def add_product(product : Products):
    products.append(product)
    return product


@app.put("/product")
def update_product(id:int, product:Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product 
            return "product added successfully"
        
    return "Product Not Found."

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Element Removed Successfully"
    return "Product not found"