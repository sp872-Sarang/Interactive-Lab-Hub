import numpy as np
import cv2
import sys
import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/SecuritySystem_Sp'
client.publish(topic,'Camera system online')

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

# Load a model imported from Tensorflow
tensorflowNet = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

from subprocess import call

#func
def speak_command(command):
  #text2speech vars
  cmd_beg= 'echo '
  cmd_end = '| festival --tts'
  Speech_cmd_start = command
  call([cmd_beg+Speech_cmd_start+cmd_end], shell = True)

thresh = 0

img = None
webCam = False
cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Resized Window', 640, 360)
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      img = cv2.imread("../data/test.jpg")
      print("Using default image.")


while(True):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape

    # Use the given image as input, which needs to be blob(s).
    tensorflowNet.setInput(cv2.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))

    # Runs a forward pass to compute the net output
    networkOutput = tensorflowNet.forward()
    
    count = 0
    # Loop on the outputs
    for detection in networkOutput[0,0]:
        score = float(detection[2])
        if score > 0.2:
            count += 1
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows

            #draw a red rectangle around detected objects
#             cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)
    
    #print(count)
    
    if(count > 1):
        client.publish(topic, "Object Detected in Apt")
        #Speech_cmd_start = 'Intruder Detected'
        #speak_command(Speech_cmd_start)
        print("User detected")
    else:
        client.publish(topic, "Apt is Safe XD")
        print("User Not detected")

    if webCam:
        if sys.argv[-1] == "noWindow":
           print("Finished a frame")
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('Resized Window',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break
    
cv2.destroyAllWindows()


