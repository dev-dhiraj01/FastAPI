
# This file will be used to crerate database schema
from sqlalchemy import Column , Integer ,String ,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):

    __tablename__ = "products"

    id = Column( Integer , primary_key = True, index = True)
    name = Column( String)
    desc = Column(String)
    price = Column(Float)
    quant = Column(Integer)