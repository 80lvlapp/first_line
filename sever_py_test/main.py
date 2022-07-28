import uvicorn

from fastapi import FastAPI


app = FastAPI(title="first-line")


@app.get("/")
async def index():
    return {"data": "Hello"}


if __name__ == "__main__":  # for dev. debugging purposes
    uvicorn.run("main:app", host="localhost", port=8000)