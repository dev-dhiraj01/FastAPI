from fastapi import  Depends , FastAPI
from models import Products
from database import session , engine 
import databases_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    count = db.query(databases_models.Products).count()
    if count == 0:
        for product in products:
            db.add(databases_models.Products(**product.model_dump()))
        db.commit()

init_db()


# @app.get("/products")
# def all_products(db : Session = Depends(get_db)):
#     # return db.query(Products).all()
#     db_products = db.query(databases_models.Products).all()
#     return db_products

@app.get("/products")
def all_products(db: Session = Depends(get_db)):
    db_products = db.query(databases_models.Products).all()
    return [
        {
            "id": p.id,
            "name": p.name,
            "desc": p.desc,
            "price": p.price,
            "quant": p.quant
        }
        for p in db_products
    ]


@app.get("/products/{id}")
def get_product_by_id(id:int,db : Session = Depends(get_db)):
    db_product = db.query(databases_models.Products).filter(databases_models.Products.id == id).first()
    if db_product:
        return db_product
        
    return "Product Not Found"


@app.post("/products")
def add_product(product : Products,db : Session = Depends(get_db)):
    db.add(databases_models.Products(**product.model_dump()))
    db.commit()
    return "Product Added Successfully."


@app.put("/products/{id}")
def update_product(id:int, product:Products,db : Session = Depends(get_db)):
    db_product = db.query(databases_models.Products).filter(databases_models.Products.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.desc = product.desc
        db_product.price = product.price
        db_product.quant = product.quant
        db.commit()
        return "Product Updated."
    else:        
        return "Product Not Found."

@app.delete("/products/{id}")
def delete_product(id: int,db : Session = Depends(get_db)):
    db_product = db.query(databases_models.Products).filter(databases_models.Products.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Element Deleted Successfully"
    else:
        return "Product not found"