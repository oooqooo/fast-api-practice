from  pydantic import BaseModel

class user(BaseModel):
    id:int
    file:str
    edits:int = 0
    lines_added:int = None