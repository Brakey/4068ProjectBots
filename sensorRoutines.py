#MTRN4068 Final Project
#By: Byron Brake, Ben Cah and Jonathan Barrett

#Sensor Routines
#All routine checks and interrupt code will be found here
#This will merely send replies of requested sensor information
#NOTE: This code does not handle any tracking of sensor data

#stopCheck will determine whether we are too close to an object to keep
#moving.
#inputs: sensor's current range and sensor's stopping range
#outputs: 1: the robot should stop, 0: the robot may continue
def stopCheck(sensorRange, stopRange):
    if sensorRange < stopRange:
        return 1
    else:
        return 0

#currentRange will return a measurement in centimetres of the current
#distance the sensor detects
#inputs: sensor's current range
#outputs: -1: if sensor is out of range or too close, 10-80: range in cm
def currentRange(sensorRange):
    #to be completed

#encoderInterrupt will count encoder rotations with interrupt
#inputs: n/a
#outputs: a value of total revolutions since being zeroed
def encoderInterrupt():
    #To be completed

#getAngle will check the current angle of the gyroscope
#inputs: current angle
#outputs: current angle in relation to initial 0 degrees
def getAngle():
    #To be completed

#setAngle will reset the current angle to 0 degrees
#inputs: current angle
#outputs: new angle as zero degrees
def setAngle():
    #To be completed

