# INFO 5435 - Final Project

#### Team Members
Sarang Pramode - sp872@cornell.edu
Olena Bogdanov - ob234@cornell.edu

## Problem 
Roosevelt Island residents(specifically Cornell Tech Students) are not aware of the RedBus schedule in realtime. The schedule is posted on a static page which can be found here, which varies based on rush hour and driver availability. From experience this has not been consistent and can lead to wait time from anywhere between 2min to 20min. 

## Big Idea
The idea is to create a local mesh network which is placed on a single strip in line of sight on west loop road which can notify users standing on the bus stop at the entrance of Cornell Tech campus.

## Timeline
- Development and implementation
- Camera System:  20 Nov
- Node-Node Communication: 18- 22 Nov
- Bus Stop Interface: 23-25 Nov
- Finalization and Testing: 25-29th Nov

## Parts Needed - Hardware
- nrf24L01
- Raspi
- Camera
- Ultrasonic Sensor/Distance Sensor
- OLED Screen

## Risks/Contingencies
Risk : Bus Not Detected Accurately Using ML model
Contingency - Object Detection Algorithm
Risk : Node Failure
Contingency : Node heartbeat packets + fall back to static notification based on expected times

## Fall-back plan
The network can serve as a communication channel to collect sensor information and display on a dashboard. 
We can create a peer to peer network to exchange information securely between two parties.

## Link To Slide : 
[LINK](https://docs.google.com/presentation/d/1d0rzevYsG6oxGAt7zeWrucS63koTa7eo6vatCob5x00/edit?usp=sharing)

## Todo: 
Contacting roosevelt island about pilot testing project  
Request letter from wendy 
Request to schedule meeting (Olena) 

Figure out interface design
ML model for vehicle detection (kaggle bus dataset) 

- https://www.kaggle.com/code/ankitp013/step-by-step-yolov3-object-detection
- https://www.kaggle.com/code/kdnishanth/bus-or-car-using-cnn-100-accuracy/data
- https://www.kaggle.com/code/ankitp013/step-by-step-yolov3-object-detection




