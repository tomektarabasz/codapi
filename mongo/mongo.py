from asyncio import events
from datetime import datetime
from models.models import Request
from pymongo import MongoClient

def connect_to_mongo_db():
    client = MongoClient("192.168.1.143", 27018)
    db = client.gps
    return [client, db]


client, db = connect_to_mongo_db()

def add_location(request: Request):
    db.events.insert_one({"name":request.name,"identity":request.identyficator, "longitude":request.longitude, "latitude": request.latitude, "time": datetime.now().strftime("%m/%d/%Y, %H:%M:%S") })
    return "ok"