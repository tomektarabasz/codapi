from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class Response(BaseModel):
    isCreated:bool = False
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Request(BaseModel):
    name:str
    identyficator:str
    longitude:float
    latitude:float