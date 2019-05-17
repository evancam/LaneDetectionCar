# LaneDetectionCar
A car that communicates with a ground station using bluetooth and provides LED feedback of lane position

Co-written with @rwierzbicki

lane_detect.py written by Eric Ashlee

# Structure

The car works as the control server as it receives will adjust steering based on input from the base station
The control server uses the RFCOMM protocol for maximum reliability

The base station works as the detection server as it will determine lane position based on images from the car 
The detection server uses L2CAP to ensure constant streaming

The two control loops are split to allow for autonomy in case of one of the 

The communication was done using bluetooth to make it a direct connection between the two systems. 
Wifi was available but there were some concerns about noise in the environment 

# Improvements

-Add proper error-checking and improve self-recovery of control loops

-Change from LED position detection to live visual feedback to the ground station and adjust controls based on this

-Re-write in C if the camera is upgraded to improve resolution and framerate
