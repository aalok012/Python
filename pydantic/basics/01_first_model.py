from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    is_active: bool
    
input_data = {'id':101, 'name': "Alok", 'is_active':True }

user= User(**input_data) #two * are used to unpack the dict
print (user)