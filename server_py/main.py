import uvicorn

from fastapi import FastAPI

from endpoints import categories, coaches, sportsman, school_endpoints, type_of_tournament_endpoints
from endpoints import tournament_endpoints
from db.base import database

# Initialize the app
app = FastAPI(title="first-line")

app.include_router(categories.router, prefix="/api/categories", tags=["categories"])
app.include_router(coaches.router, prefix="/api/coach", tags=["coaches"])
app.include_router(sportsman.router, prefix="/api/sportsmen", tags=["sportsman"])
app.include_router(school_endpoints.router, prefix="/api/rest-schools", tags=["schools"])
app.include_router(type_of_tournament_endpoints.router, prefix="/api/type-of-tournaments", tags=["type-of-tournaments"])
app.include_router(tournament_endpoints.router, prefix="/api/tournaments", tags=["tournaments"])


@app.get("/")
async def index():
    return {"data": "Hello"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":  # for dev. debugging purposes
    uvicorn.run("main:app", host="localhost", port=8000)
