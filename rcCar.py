#MTRN4068 Final Project
#By: Byron Brake, Ben Cah and Jonathan Barrett

#rcCar
#This file controls the setup and any sensor tracking for the 4 wheel
#steered RC car
#NOTE: Only RC car controls are here - omni car cannot reach this code

import RPi.GPIO as GPIO

#setup initialises all pins for the rcCar - inputs and outputs
#inputs: n/a
#outputs: n/a
def setup():
    GPIO.setmode(GPI.BCM)
    

#forward moves the vehicle forward at the current speed
#inputs: n/a
#outputs: n/a
def forward():
    #To be completed

#reverse moves the vehicle backwards
#inputs: n/a
#outputs: n/a
def reverse():
    #To be completed

#turn will move the vehicle in the given direction at an angle whilst
#moving forward
#inputs: turn angle - how far from 0-x degrees, direction - left or right
#outputs: n/a
def turn(turnAngle, direction):
    #To be completed

#stops the vehicle and but doesn't adjust steering angle
#inputs: n/a
#outputs: n/a
def stop():
    #To be completed

#resetAngle will reset the vehicles steering to the 0 point
#inputs: 
#outputs: 
def resetAngle():
    #To be completed

#getSpeed checks the speed given by the user and provides it
#inputs: n/a
#outputs: n/a
def getSpeed():
    #To be completed

#changes the speed the vehicle is moving at
#inputs: newSpeed - new speed between 0-255 to change to
#outputs: n/a
def setSpeed(newSpeed):
    #To be completed
