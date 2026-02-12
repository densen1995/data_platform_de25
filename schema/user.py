from pydantic import BaseModel

class UserSchema(BaseModel): #(input model)
    username:str
    password:str
    is_enabled:bool

class UserSchemaResponse(BaseModel): #(output model)
    username: str