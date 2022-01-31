from fastapi import FastAPI 
import pydantic
from pydantic import BaseModel
import redis

class input_param(BaseModel):
    latitude: float 
    longitude: float 

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
user1.name = 'user1' 
user1_dict = user1.dict()

user2 = db_roam_location()
user2.roam_db_id = 2
user2.activity = 'MOVING'
user2.latitude = 26.850000
user2.longitude = 80.949997
user2.recorded_at = '13:00' 
user2.name = 'user2' 
user2_dict = user2.dict()

def redis_string(t1,t2):
    global user1_dict
    global user2_dict
    r = redis.Redis(host='localhost',port=6379)
    r.hmset("user1",user1_dict)
    r.hmset("user2",user2_dict)
    r.geoadd("users",[user1.longitude,user1.latitude,'user1'],nx=True,xx=False) 
    r.geoadd("users",[user2.longitude,user2.latitude,'user2'],nx=True,xx=False)
    name =  r.georadius("users", t1, t2, 500)
    name = name[0]
    name = name.decode('utf-8')
    return r.hgetall(name)


app = FastAPI()
@app.post('/')
def fnc(inp1: input_param):
    longitude = inp1.longitude 
    latitude  = inp1.latitude 
    return redis_string(longitude,latitude)






