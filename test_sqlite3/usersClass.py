from pydantic import BaseModel
from typing import Optional



class User(BaseModel):

    id : Optional[int]
    name : str
    email : str

    def __init__(self, tuple):
        self.id , self.name, self.email, = tuple 

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
