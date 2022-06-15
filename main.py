import uvicorn
from .models.models import Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, params
from .mongo.mongo import add_location

app = FastAPI()
origins = [
    "https://localhost:4200",
    "http://localhost:4200",
    "http://192.168.1.143:8000",
    "http://192.168.1.17:4200",
    "http://192.168.1.17:80",
    "http://192.168.1.17:8000",
    "http://89.65.210.136/*",
    "http://89.65.210.136:*",
    "http://89.65.210.136:8000",
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return({"id": "Here will be api"})


@app.post("/position", response_model=Response)
def send_position(request: Request):
    name = request.name
    identyficator = request.identyficator
    longitude = request.longitude
    latitude = request.latitude
    add_location(request)
    result = Response()
    print(result)
    return result


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=7000)
