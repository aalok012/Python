from typing import List
from pydantic import BaseModel 

class Address(BaseModel):
    street: str
    city:str
    postal_code: str
    
class User(BaseModel):
    id:int
    name: str
    address: Address
    
address= Address(
    street="sokdnf",
    city="ishfg",
    postal_code="sknfp"
)