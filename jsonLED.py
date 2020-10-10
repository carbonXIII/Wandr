
import RPi.GPIO as GPIO
import board
import busio
from time import sleep
from sys import argv
import json
import requests


GPIO.setmode(GPIO.BCM)

camLED = 11
micLED = 9
mainLED = 10

camSwitch = 22
micSwitch = 27
mainSwitch = 17


GPIO.setup(camLED,GPIO.OUT) #script LED
GPIO.setup(micLED,GPIO.OUT) #script LED
GPIO.setup(mainLED,GPIO.OUT) #script LED



GPIO.setup(camSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP) #status switch input
GPIO.setup(micSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP) #status switch input
GPIO.setup(mainSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP) #status switch input


def switchLED(pin,state):
    if state:
        GPIO.output(pin,GPIO.HIGH)
        print('changing to hi')
    else:
        GPIO.output(pin,GPIO.LOW)
        print('changing to low')
        
def stateString(state):
    if state:
        return 'on'
    else:
        return 'off'


sleepTime =0.5
switchLED(camLED,True)
sleep (sleepTime)
switchLED(camLED,False)
sleep (sleepTime)

switchLED(camLED,True)
sleep (sleepTime)
switchLED(camLED,False)
sleep (sleepTime)

switchLED(micLED,False)
switchLED(camLED,False)
switchLED(camLED,False)

while True:
    micState = GPIO.input(micSwitch)
    switchLED(micLED,micState)
    
    camState = GPIO.input(camSwitch)
    switchLED(camLED,camState)
        
    mainState = GPIO.input(mainSwitch)
    switchLED(mainLED,mainState)
    
    data2 = {
    "main": stateString(mainState),
    "cam": stateString(camState),
    "mic": stateString(micState),
    }
    
    response = requests.post('https://httpbin.org/post',data2)
    print("status code:",response.status_code)
    print("Printing entire post request")
    print(response.json())

sleep(1)

GPIO.cleanup()


