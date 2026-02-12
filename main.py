from typing import Union
from fastapi import FastAPI, status

import requests

from schema.fox import FoxSchema
from schema.user import UserSchema, UserSchemaResponse

#client
userList: list[UserSchema]= [
    UserSchema(username="Benny", password="123", is_enabled=True),
    UserSchema(username="John", password="123", is_enabled=True),
    UserSchema(username="Roy", password="xyz", is_enabled=True),
] 

##fatsapi
app = FastAPI(title= "My First API APP") #creates api application , app receives the http request and decides fucntions to run 

@app.get("/")  #root endpoint, decorator that runs function when a request is sent 
def root():
    return{"Hello": "World"} #FastAPI automatically converts to json and returns http status 200 ok  


@app.get("/items/{item_id}")
def get_item(item_id: int, color: Union[str, None] = None):
    return{"item_id": item_id, "color":color}

@app.get("/users", response_model=list[UserSchemaResponse]) #filters output auto, but doesn't return password 
def get_users() -> list[UserSchemaResponse]:
    return userList

@app.post("/users", response_model=UserSchema)
def post_user(user:UserSchema):
    userList.append(user)
    return user

@app.post(
    "/users",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED

)
def post_user(user:UserSchema) -> UserSchema:
    userList.append(user)
    return user

@app.get("/fox")
def get_fox() ->FoxSchema:
    response=requests.get("https://randomfox.ca/floof/")
    result_json= response.json()
    print(f"DEBUGGING{response}")

    fox= FoxSchema(**result_json)
    return fox