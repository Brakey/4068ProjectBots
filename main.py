#MTRN4068 Final Project
#By: Byron Brake, Ben Cah and Jonathan Barrett

#Main File
#All execution code will be found here along with
#any necessary information and basics for setup.

#The 2 vehicle types will be referred to as:
    #rcCar or 0
    #and or 1
    #omniCar
#Any reference to the vehicles will be as these two names within the code
#For further information regarding both of these vehicles please see the
#readme.

#External modules
import time
import RPi.GPIO as GPIO
import cv2

#Internal Files
import sensors
import opencv
import bluetooth
import sensorRoutines
import rcCar
import omniCar
import control
import autoControl

#Variables
carType = -1

#vehicleSelect will allow for the correct vehicle code to be executed
#inputs: 0 - rcCar or 1 - omniCar, -1 - no car selected
#outputs: Either return for a reselect if -1 is selected or change carType to
#the correct variable
def vehicleSelect(vehicle):
    if vehicle == 0:
        carType = 0
    elif vehicle == 1:
        carType = 1
    else:
        raise Exception("Vehicle input not valid, try again")

def vehicleStart(carType):
    if carType == 0:
        rcCar.setup()
    elif carType == 1:
        omniCar.setup()
    else raise Exception("Vehicle not assigned")

#When we shutdown we ensure that we have clean pin outputs
GPIO.cleanup()