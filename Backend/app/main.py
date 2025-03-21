from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.mongo import mongo
from app.api import home, movies


@asynccontextmanager
async def lifespan(_: FastAPI):
    await mongo.connect()
    yield
    await mongo.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(home.router, prefix="/home", tags=["Home"])
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
