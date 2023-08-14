from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.requests import Request

app = FastAPI()

app.mount("/AI_Challenge", StaticFiles(directory="AI_Challenge"), name="AI_Challenge")

@app.get("/")
async def read_root():
    return FileResponse("index.html")

@app.get("/api/data")
def get_data():
    data = {"message": "Hello from the API!"}
    return data
