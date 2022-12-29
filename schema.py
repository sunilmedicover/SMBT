from pydantic import BaseModel
from datetime import date

class Don1(BaseModel):
    name:str
    country:str
    country_code:int
    state:str
    state_code:int
    city:str
    pincode:int
