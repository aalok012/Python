from pydantic import BaseModel,Field,  computed_field

class Product(BaseModel):
    price: float
    quantity:int
    
    @computed_field
    @property
    def total_price(self)-> float:
        return self.price *self.quantity
    
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float
    
    @computed_field
    @property
    def total_amt(self)-> float:
        return self.nights *self.rate_per_night
    
booking= Booking(
    user_id= 58,
    room_id= 5000,
    nights= 2,
    rate_per_night= 500
    
)
print(booking.total_amt)