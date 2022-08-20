import uvicorn
from fastapi import FastAPI
from db.database import engine
from db import models
from routers import categories_router, coach_router, school_router, sportsman_router
from routers import type_of_tournaments_router, tournament_router

app = FastAPI(title="First-line")


@app.get("/")
async def index():
    return {"data": "Hello"}


app.include_router(categories_router.router)
app.include_router(coach_router.router)
app.include_router(school_router.router)
app.include_router(sportsman_router.router)
app.include_router(type_of_tournaments_router.router)
app.include_router(tournament_router.router)

models.Base.metadata.create_all(engine)

# app.include_router(value_categories_endpoints.router, prefix="/api/value-category", tags=["value-category"])

if __name__ == "__main__":  # for dev. debugging purposes
    uvicorn.run("main:app", host="localhost", port=8000)
