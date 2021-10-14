#MTRN4068 Final Project
#By: Byron Brake, Ben Cah and Jonathan Barrett

#Sensor Code and setup
#All sensor pins, and variables for distance

import RPi.GPIO as GPIO

#Distance Tracking Variables
stopRange = 20 #Collision Range for stop
maxRange = 255 #Maximum distance from range finder
minRange = 2 #Minimum when sensor will no longer operate correctly

#Sensor Input Pins - Universal
rangeFinder = 3

#Sensor Input Pins - omniCar
enc1 = 7
enc2 = 8
enc3 = 9
mpuSDA = 10
mpuSCL = 11

#Output Pins rcCar
rcSteer = 4
rcDrive = 5

#Output  Pins omniCar
omni1 = 4
omni2 = 5
omni3 = 6
