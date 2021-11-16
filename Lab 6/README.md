# Little Interactions Everywhere

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)


### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***
![lab6-2](https://user-images.githubusercontent.com/32943943/141924744-abbaee4b-7ac3-41a5-b982-d28fe286e451.jpg)
![lab6-3](https://user-images.githubusercontent.com/32943943/141924749-a3ce721b-4ac3-4a93-899c-a6acb4d98b11.jpg)

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***


### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***


### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.
<br>What is it? A way to connect distant couples/parents and children. The idea is to use a soft cat's paw to pat the user's hand whenever they press a button. This is a subtle way for someone to say that they’re thinking about the other person without having to video call or text message, which is especially useful when they’re busy or in meetings. 

<br>Ideally, we would have wanted the cat paw to be a discreet wearable, but for our prototype, we’ve primarily focused on showing how it works. This is currently also a pair system since we want the users to be intentional about who they are thinking of.

<br>This idea is also inspired by Yujie Tao and Yiran Zhao’s research project.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?
<br>There are two key components for each user:
<br>1. Button to move the paw of their counterpart. This button sends a message saying “pressed” using mqtt.
<br>2. “Paw” attached to a servo, controlled remotely by the button from their counterpart. The paw will move whenever a message is received with the string “pressed”

<br>Person A will send button pressed messages to the `person_b` topic and subscribe to `person_a` topic to listen to button pressed messages from Person B. Vice versa for Person B - they will send button pressed messages to `person_a` topic and subscribe to `person_b` topic to listen to button pressed messages from Person A. Effectively, one holds the remote control for the other’s paw.
![lab6-4](https://user-images.githubusercontent.com/32943943/142012236-3b74eb86-6f10-46dd-b0aa-c9393ae457e6.jpg)

**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?
<br>We were inspired by natural ways humans show care, and thus decided to use the patting gesture to show that one is thinking of the other. Following the idea of shaking hands with a cat’s paw, a common act people do, we also added a button below our device’s paw that the user can press to show that they acknowledge the thought. To send a pat, we symbolized it with button presses since it is a similar gesture to patting. There are only two buttons that control the system. User A presses the button to send the affection to User B and User B can press User A to indicate that he/she has received the affection. 

Below are some photos we took of the prototyping process:
Rigid wire poked through a cotton string to easily form the paw’s shape
![image](https://user-images.githubusercontent.com/32943943/142012533-67686f3f-0d42-4448-8b48-45ac1f5a4c50.png)
Button attached to the bottom of the paw with an invisible cord
![image](https://user-images.githubusercontent.com/32943943/142012617-bf25a456-d683-4dd2-83c6-c07bbc74951b.png)
Overall system prototype
![image](https://user-images.githubusercontent.com/32943943/142012656-39707730-8c23-4468-9935-4fae79352ba7.png)

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.
<br>Video prototype: https://drive.google.com/file/d/1MSA06REz-eNHIBchK-0AbnfdhdFsCtiz/view

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

