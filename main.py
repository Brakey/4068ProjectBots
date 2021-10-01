#MTRN4068 Final Project
#By: Byron Brake, Ben Cah and Jonathan Barrett

#Main File
#All execution code will be found here along with
#any necessary information and basics for setup.

#The 2 vehicle types will be referred to as:
    #rcCar
    #and
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


#When we shutdown we ensure that we have clean pin outputs
GPIO.cleanup()