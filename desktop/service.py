import flask
from flask import Flask
from pynput.keyboard import Key, Controller
import time

api = Flask(__name__)

keyboard = Controller()

state = {
    'main': False,
    'cam': True,
    'mic': True,
}

def key_sequence(keys, pause=0.1):
    for key in keys:
        keyboard.press(key)
    time.sleep(pause)
    for key in reversed(keys):
        keyboard.release(key)

def cam_switch():
    key_sequence([Key.alt_l, 'c'])
    state['main'] = not state['main']

def toggle_cam():
    key_sequence([Key.alt_l, 'v'])
    state['cam'] = not state['cam']

def toggle_mic():
    key_sequence([Key.alt_l, 'a'])
    state['mic'] = not state['mic']

def parse_toggle(s):
    return 'on' in s.lower()

@api.route('/update', methods=['POST'])
def update():
    '''
    Example

    {
    'main': ON
    'cam': OFF
    'mic': OFF
    }
    '''

    print(flask.request.json)
    j = flask.request.json

    if not j:
        flask.abort(400)
        return

    if state['main'] != parse_toggle(j['main']):
        cam_switch()

    if state['cam'] != parse_toggle(j['cam']):
        toggle_cam()

    if state['mic'] != parse_toggle(j['mic']):
        toggle_mic()

    return {'resp': 'SUCCESS'}
