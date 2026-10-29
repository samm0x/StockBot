from pydantic import BaseModel
from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)

# class Dolar(BaseModel):
#     name: str
