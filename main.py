from fastapi import FastAPI
from app.api.query_api import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Project Running"}