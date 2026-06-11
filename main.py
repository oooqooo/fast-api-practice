from fastapi import FastAPI,Request
from raj import l
from pydantic import BaseModel
import pydantic
from ma import user
app=FastAPI()



@app.get("/home1")
def home():
    return l

@app.get("/home/{par}")
def name(par:int):
    for i in  l:

        if i.get("id")==par:
            return i
    return "not found111111111111111111111"

@app.get("/welcome")
def welcome(nam:Request):
    dict1=nam.query_params
    return f"welcome to fast api, {dict1.get('name')} {dict1.get('age')}!"


@app.post("/create")
def create(request1:user):
    dict1=request1.model_dump()
    print(dict1)
    l.append(dict1)
    return "created successfully"


@app.put("/update/{par}")
def update(par:int, request1:user):
    for i in l:
        if i.get("id") == par:
            l.remove(i)
            dict1=request1.model_dump()
            print(dict1)
            l.append(dict1)
            return "updated successfully"
    return "not found"

@app.delete("/delete/{par}")
def delete(par:int):
    for i in l:
        if i.get("id") == par:
            l.remove(i)
            return "deleted successfully"
    return "not found"