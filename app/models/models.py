from pydantic import BaseModel, computed_field

class User(BaseModel):
    name: str
    age: int