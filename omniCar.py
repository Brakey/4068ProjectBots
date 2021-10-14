#MTRN4068 Final Project
#By: Byron Brake, Ben Cah and Jonathan Barrett

#omniCar
#This file sets up and controls all sensors and outputs for the 3 wheel
#omni directional vehicle, the mechanical design of this will be
#displayed within the repo to understand how this vehicle works
#NOTE: Only 3 wheel omni car controls are here - rcCar cannot reach this code

import RPi.GPIO as GPIO

motorA = 0
motorB = 2
motorC = 3
encA = 1
encB = 4
encC = 5
rangeSensor = 26
scl = 8
sda = 9


#setup initialises all pins for the omniCar - inputs and outputs
#inputs: n/a
#outputs: n/a
def setup():
    GPIO.setmode(GPI.BCM)
    GPIO.setup(motorA, GPIO.OUT)
    GPIO.setup(motorB, GPIO.OUT)
    GPIO.setup(motorC, GPIO.OUT)
    GPIO.setup(encA, GPIO.IN)
    GPIO.setup(encB, GPIO.IN)
    GPIO.setup(encC, GPIO.IN)
    GPIO.setup(rangeSensor, GPIO.IN)

#reverse moves the vehicle forwards
#inputs: 
#outputs: 
def forward():
    #To be completed

#reverse moves the vehicle backwards
#inputs: n/a
#outputs: n/a
def reverse():
    #To be completed

#reverse moves the vehicle sideways
#inputs: 
#outputs: 
def strafe():
    #To be completed

#rotates the vehicle in the input direction until stopped
#inputs: direction: clockwise or anticlockwise
#outputs: n/a
def rotate(direction):
    #To be completed

#stops the vehicle moving
#inputs: n/a
#outputs: n/a
def stop():
    #To be completed

#gets the speed from the app
#inputs: n/a
#outputs: speed: new speed of the vehicle
def getSpeed():
    #To be completed

#updates the speed the vehicle travels at between 0-255
#inputs: newSpeed - new speed between 0-255 to change to
#outputs: n/a
def setSpeed():
    #To be completed