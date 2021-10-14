#MTRN4068 Final Project
#By: Byron Brake, Ben Cah and Jonathan Barrett

#OpenCV
#All openCV processing and tracking will be in this file
#It will be in callable functions that process what is required

#cameraSetup will initialise the communication with the camera and handles
#all openCV setup
#inputs: none
#outputs: none
def cameraSetup():
    #To be completed

#getCameraFeed will create a raw version of the camera and resize
#the image to a defined size
#inputs: sizeX - the horizontal length of video, sizeY - vertical height of
#the video
#outputs: camera feed which is resized but not cropped
def getCameraFeed(sizeX, sizeY):
    #To be completed

#sendCameraFeed will pass the camera from getCameraFeed through to the app
#using the bluetooth abilities
#inputs: n/a
#outputs: Camera feed to app
def sendCameraFeed():
    #To be completed

#objectDetect will detect an object of the specified type
#inputs: objectType - the kind of object that will be searched for, a list
#will be provided here later
#outputs: 0 - if object is not detected, 1- if object is detected
def objectDetect(objectType):
    #To be completed