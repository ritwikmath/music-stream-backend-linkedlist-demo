from fastapi import FastAPI
from router import music_router

app = FastAPI()

app.include_router(music_router)