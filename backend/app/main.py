from database import init_models
from fastapi import FastAPI
from routers import game

app = FastAPI()


app.include_router(game.router)


@app.on_event("startup")
async def on_startup():
<<<<<<< HEAD






=======
>>>>>>> 89ffce0fe03c4f064d2e8d6e2c97650e6c25eb4c
    await init_models()


@app.get("/")
async def root():
    return {"message": "Hello World"}
