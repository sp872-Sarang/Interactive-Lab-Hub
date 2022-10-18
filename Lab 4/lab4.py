import time
import board
import busio
import qwiic_button
import random

from subprocess import call

import adafruit_mpr121 #capacitive touch

#init
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
my_button = qwiic_button.QwiicButton()


#func
def speak_command(command):
  #text2speech vars
  cmd_beg= 'echo '
  cmd_end = '| festival --tts'
  Speech_cmd_start = command
  call([cmd_beg+Speech_cmd_start+cmd_end], shell = True)

GR_insult1_path = 'GR_insult1.mp3'
def play_audio(GR_insult1_path):
  cmd_beg= 'mpg321 '
  call([cmd_beg+GR_insult1_path], shell = True)


#text2speech vars
# cmd_beg= 'echo '
# cmd_end = '| festival --tts'

Speech_cmd_start = 'Game Ready , Begin Operation '
speak_command(Speech_cmd_start)

Speech_cmd_time = 'You have 2 minutes to save the patient'
speak_command(Speech_cmd_time)

#progam vars
Body_Harm_Counter = 0
Lives = 10
BodyPartTracker = [1,1,1,1,1,1]

GR_insult_dict = {
  1:"GR_insult1.mp3",
  2:"GR_insult7.mp3",
  3:"GR_insult8.mp3",
  4:"GR_insult4.mp3",
  5:"GR_insult5.mp3",
  6:"GR_insult6.mp3",
  7:"GR_insult7.mp3",
  8:"GR_insult8.mp3",
  9:"GR_insult9.mp3",
}

while True:

  old_count = sum(BodyPartTracker)

  if Body_Harm_Counter >= Lives :
    print(" You have failed to save the patient, Press Button to reset the game")
    play_audio('GR_insult10.mp3')
    speak_command("You have lost the patient")
    speak_command("Press the reset button to try again")

    while(True):
      if my_button.is_button_pressed() == True:
          print("\nThe game is reset , Reset Button Pressed")
          Body_Harm_Counter = 0


          speak_command("We have a new patient for you! Lets try again")

          break
      #print("Awaiting Reset")
      time.sleep(0.02)


  for i in range(6): # 0-5 senses if a part is touched
      if mpr121[i].value:

        while(mpr121[i].value): # prevents debouncing
          continue

        print(f"Terminal {i} touched")

        #speak_command("Ow, That hurt")

        GR_insultpath = GR_insult_dict[random.randint(1,9)]
        play_audio(GR_insultpath)

        #sanity check
        #print("GR insult path : ", GR_insult_dict[random.randint(1,5)])

        Body_Harm_Counter += 1
        print(f"Patient feels pain : Body part {i} touched!")
        print("You have : {} Lives remaining".format(Lives - Body_Harm_Counter))

  for i in range(6,12): # 6-11 senses if a part is lifted
      if not mpr121[i].value:
        BodyPartTracker[i - 6] = 0
      else:
        BodyPartTracker[i - 6] = 1

      new_count =  sum(BodyPartTracker)

  if(old_count != new_count):
    print("Body parts remaining to extract : ",sum(BodyPartTracker))

    old_count = new_count

  if my_button.is_button_pressed() == True:
    print("\nThe game is reset , Reset Button Pressed")
    Body_Harm_Counter = 0

    speak_command("We have a new patient for you! Lets try again")


  time.sleep(0.02)




