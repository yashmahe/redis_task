from fastapi import FastAPI 
import pydantic
from pydantic import BaseModel
from pymongo import MongoClient
import ssl
import socket

cluster = MongoClient("mongodb+srv://yashm:yashmahe@cluster0.c5wwa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
db = cluster["db_roam_location"]
collection = db["user_details"]

class db_roam_location(BaseModel):
    roam_db_id: int=0
    activity: str=None
    latitude: str=None 
    longitude: str=None
    recorded_at: str =None
    name: str=None

user1 = db_roam_location()
user1.roam_db_id = 1
user1.activity = 'MOVING'
user1.latitude = 26.449923
user1.longitude = 80.331871
user1.recorded_at = '12:30'
user1.name = 'user1' #using 24 hrs time format
user1_dict = user1.dict()
collection.insert_one(user1_dict)

user2 = db_roam_location()
user2.roam_db_id = 2
user2.activity = 'MOVING'
user2.latitude = 26.850000
user2.longitude = 80.949997
user2.recorded_at = '13:00' 
user2.name = 'user2' #using 24 hrs time format
user2_dict = user2.dict()
collection.insert_one(user2_dict)