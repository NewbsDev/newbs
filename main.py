from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import red_stars as rs
import white_stars as ws


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def root():

    return {'message': 'Hey! We\'re trying to work here!'}


@app.get('/red_stars')
async def red_stars():

    return


@app.get('/white_stars')
async def white_stars():

    return
