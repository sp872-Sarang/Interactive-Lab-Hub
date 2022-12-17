INFO 4325: Interactive Device Design 
# RIOC Bus Tracker Project
Group Members: Sarang Pramode (sp872) & Olena Bogdanov (ob234) 

### Problem Statement 
Roosevelt Island residents(specifically Cornell Tech Students) are not aware of the RedBus schedule in realtime. The schedule is posted on a static page which can be found here, which varies based on rush hour and driver availability. From experience this has not been consistent and can lead to wait time from anywhere between 2min to 20min.

### Problem Description
We hope to create a device people can interact with to be aware of bus schedules. We also hope to study user interactions with the red bus, specifically, learn the number of students using the bus and the pain points as to when they don't want to use it.

### User Research 
To begin our project, we reached out to a few friends who live in the house to ask them about their experiences taking the RIOC bus. Most of them prefer to walk to Main Street because it’s faster, and generally avoid taking the red bus. In general, people seemed to be averse to taking the RIOC bus for the sake of efficiency - they were unsure of where the bus is, when it would arrive, and preferred to avoid relying on the 15-minute estimate offered by RIOC. However, two students mentioned that they would be more likely to travel via bus if the bus schedule offered more detailed information on this mode of transportation. Overall, it seems that a lack of awareness about the bus, avoidance of relying on estimated bus schedules, and a preference for walking are some of the pain points that residents of Roosevelt Island experienced when it comes to engaging with the RIOC bus system. In conclusion, there are a few main things we wanted to keep in mind going forward: [1] There exists a lack of information on bus times, which leads to erratic wait times for students, [2] Students are not aware that an online bus schedule exists, and [3] students reported that they would take the bus if they anticipated its arrival, however it was the lack of available information which caused the greatest amount of inconvenience and uncertainty.

### Storyboard & Verplank Diagram 
For our [storyboard](https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/fe5d31931dcc0aeeabb3734472247a36b69404b5/Final%20Project/assets/storyboard.png) and [verplank](
https://github.com/sp872-Sarang/Interactive-Lab-Hub/blob/fe5d31931dcc0aeeabb3734472247a36b69404b5/Final%20Project/assets/verplank.png) diagram our goal was to convey the inefficiencies that emerge when interacting with the bus network. We re-create an experience many Roosevelt Island residents can relate to; traveling to the bus stop, only to experience odd departure and arrival times, ultimately reducing the users ability to interact with the system. The breakthrough occurs when our subject, Jack, notices a new, innovative product that resolves this issue - the bus tracker system, which ensures that users have the best understanding of when and where to catch the bus. 



## Ideation: Part 1: Prototypes 
The idea is to create a local mesh network which is placed on a single strip in line of sight on west loop road which can notify users standing on the bus stop at the entrance of Cornell Tech campus.

### Detection Node 
We considered a few factors when designing the prototype for the detection node. First, we wanted to make sure that the detection node worked for different environments - our first course of action would be to pilot-test the product, meaning that the design specifications for the detection node housing, and the included components would be different from the final product. 

The first prototype diagram, we focused on designing a product that would be possible to implement on a short-term basis, and as a result, we required a battery pack to be installed within the detection node. It is segmented into three major components: the battery pack, central pi unit, and the webcam. As the permanent installation would not require a battery pack, the final component would be much smaller. 

### Communication Node 
We emulated a bus arrival using a flag which was changed manually. We used this prototype to develop the state diagram and data packets and test any bugs when designing the system. Ultimately, we decided not to incorporate it into the final prototype as the screen wasn't the correct size - users found it difficult to see and interact with. Our nex steps were to implement a dashboard which can accessed by scan via the users mobile device. 

[Video | Prototype Testing | Bus Arrival Emulation](https://drive.google.com/file/d/1RdR2YJqAdSTYUIs21w_4qgJ3VvrxD971/view?usp=sharing)

[Video | Functional Check-In](https://drive.google.com/file/d/1C4MjyItW-Z7OiaSUTtsryfwuJhHPJi3L/view?usp=sharing)

### Object Recognition: Initial model tests & results
This project is focused on real-time object tracking of the RIOC bus, using computer vision and machine learning for image processing. We explored multiple methods for facilitating real-time, accurate object detection. 

The first system used the YOLO object detection model, which is capable of frame-by-frame object recognition across 80 classes. This model is simple, lightweight, and easy to implement, and it performed well during the initial functional check-in. In order to facilitate the interaction between YOLO and the Raspberry Pi, we focused on using BerryNet, an open-source library that creates a gateway between edge devices and deep learning models. However, after encountering a Berry-side technical incompatibility, we moved to implementing a different deep-learning / pi architecture for this project. 

In order to complete image detection, our starting point was the YOLO model, which is pre-trained to detect a bus, among other objects. We tested our starting model on RIOC bus images, which worked well and offered a great starting point that would allow us to integrate the model into the final project. 


## Ideation: Part 2: Results 
In this section, we describe the outcome of the first stage and provide a final overview of the bus detection system. 

### Node State Diagram 
After developing an initial prototype and implementing node-to-node communication, we implemented the following state diagrams for the [interface] and [detection] nodes.























