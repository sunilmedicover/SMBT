from fastapi import FastAPI,HTTPException,status
from models import Data
from mongoengine import *
from schema import Don1
import json
from fastapi import Query
from mongoengine.queryset.visitor import Q

app=FastAPI()
# uploading the data
connect(db="hrms",host="localhost",port=27017)
@app.post("/data imported")
def ge(De:Don1):
        a=Data(emp_id=Data.objects.count()+1,name=De.name,country=De.country,country_code=De.country_code,state=De.state,state_code=De.state_code,city=De.city,pincode=De.pincode)
        d=a.save()
        return {"inserted":d}

# Displaying all countrys data 
@app.get("/get all the countrys")
def asd():
    data=[{"Error":"False","message":"Data found"},["all countrylist"]]
    r=Data.objects().to_json()
    data_list=json.loads(r)
    for d in data_list:
        data.append(d)
        
    if not {"Responces":data}:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The user id already created")
    return {"Responces":data}

# Displaying state wise data
@app.get("/get data in state")
def sta(state_code:int):
    data=[{"Error":"False","message":"Data found"},["state_list"]]
    r=Data.objects.filter(state_code=state_code).to_json()
    ban=json.loads(r)
    data.append(ban)
    if not {"Responces":data}:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The user id already created")
    return {"Responces":data}

# Displaying country wise data
@app.get("/get the data country")
def cou(countrycode:int):
    data=[{"Error":"False","message":"Data found"},["countrylist"]]
    r=Data.objects.filter(country_code=countrycode).to_json()
    jan=json.loads(r)
    data.append(jan)
    return data




