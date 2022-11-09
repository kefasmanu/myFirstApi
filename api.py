from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title = 'MY FASTAPI')

#FLASK WAY
@storage.get('/')# Route
def index():
    return 'This is KEFAS MANU GALADIMA'


@storage.get('/today')#route with GET method
def today():
    return str(datetime.now())

@storage.get('/mynames')
def names(first_name: bool=False, last_name: bool=False):
    full_name =""
    
    if first_name:
        full_name += "KEFAS"
    if last_name:
        full_name +=" GALADIMA"
    if full_name:
        full_name = "KEFAS GALADIMA"
    return full_name
    