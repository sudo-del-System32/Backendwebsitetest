from pydantic import BaseModel
from typing import Optional



class User(BaseModel):

    id : Optional[int]
    name : str
    email : str

    def __init__(self, tuple):

        id , name, email = tuple 
        super().__init__(id=id, name=name, email=email)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
