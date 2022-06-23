from flask import Flask

import red_stars as rs
import white_stars as ws


app = Flask(__name__)

@app.route('/')
async def root():

    return {'message': 'Hey! We\'re trying to work here!'}


@app.route('/welcome')
async def welcome(rndm_place: str = 'sideshow') -> dict:

    return {'message': f'Welcome to the {rndm_place}.'}


@app.route('/red_stars')
async def red_stars() -> dict:

    return {'message': 'Don\'t forget your miners.'}


@app.route('/white_stars')
async def white_stars() -> dict:

    return {'message': 'Get ready to rumble!'}

if __name__ == '__main__':
    app.run()