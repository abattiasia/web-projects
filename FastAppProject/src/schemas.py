# schemas.py
# pydantic : type hint 3.6
from pydantic import BaseModel

# create , update
class ToDoSchemaIn(BaseModel):
    title: str
    description: str
    completed: bool = False

# get list, details
class ToDoSchemaOut(BaseModel):
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True
