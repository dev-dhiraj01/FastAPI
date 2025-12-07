from pydantic import BaseModel

class Products(BaseModel):
    id: int
    name: str
    desc: str
    price: float
    quant: int

    # def __init__(self,id: int,name: str,desc: str,quant: int):
    #     self.id = id
    #     self.name = name
    #     self.desc = desc
    #     self.quant = quant
        