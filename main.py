from fastapi import FastAPI
from app.routers import comments

app = FastAPI()

app.include_router(comments.router)
