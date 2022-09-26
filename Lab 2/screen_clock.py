import time
import math
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return hours,mins,sec #"Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

#global Vars
start = time.time()
Budget = 100
Spent = 0

while True:
    # Draw a black filled box to clear the image.
    #draw.rectangle((0, 0, width, height), outline=0, fill=0)
    if not buttonA.value and  not buttonB.value:
        Budget = 100
    
    if buttonA.value and not buttonB.value:  # just button B pressed
        
        #disp.fill(color565(255, 255, 255))  # set the screen to white
        #draw.rectangle((0, 0, width, height), outline=0, fill=0)
        
        #while(buttonA.value and not buttonB.value): #button A not pressed
        #counter = time.time()
        #h,m,s = time_convert(counter-start)
 
        #draw.text((0, 30), "Timer: "+"H: "+str(h)+" M: "+str(m)+" S: "+str(int(s)),font=font, fill=(255, 0, 0))
        
        #Button B  reduced money by 5
        #Budget -= 5
        Spent += 5
        #if Budget < 0:
            #Budget = 0
    
    if not buttonA.value and buttonB.value:  # just button B pressed
        #Button A  increased money by 5
        Spent -= 5
    
    if buttonA.value and  buttonB.value: #if neither are pressed
        
        y = top
        
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        
        curhour = int(time.strftime("%H"))
        curmin = int(time.strftime("%M"))
        cursec = int(time.strftime("%S"))
        
        #draw hour bar
        line_0 = 'Hrs:'
        draw.text((0, 0 + y),line_0, font=font, fill = (255, 0, 0))
        line_0size_x = font.getsize(line_0)[0]

        hbar_width = 24
        
        draw.rectangle((line_0size_x, 0 + y, 24 + 9*curhour, hbar_width + y), outline=1, fill=(255, 0, 0))
        draw.text((line_0size_x+5, 0), str(curhour), font=font, fill = "#FFFFFF")
        
        y += hbar_width        
        
        
        line2 = "Budget of the day : "+str(Budget)
        draw.text((0, y + 10), line2, font=font, fill="#FFFFFF")
        y += font.getsize(line2)[1]
        
        
        Val_tosub_permin = 4.1
        Total_valToSub = Val_tosub_permin*curhour
        RemaingBudget = float(Budget) - Total_valToSub
        
        line3 = "Remaining Money : " + str(RemaingBudget)
        draw.text((0, y + 10), line3, font=font, fill="#FFFFFF")
        y += font.getsize(line3)[1]
        
        line4 = "Spent : " + str(Spent)
        
        if(Spent >= RemaingBudget):
            draw.text((0, y + 10), line4, font=font, fill=(255,0,0))
        else:
            draw.text((0, y + 10), line4, font=font, fill=(0,255,0))

        y += font.getsize(line4)[1]
        
        
        steps = 60
        rec_width = width/steps
        
        draw.rectangle((0,30+y, rec_width*cursec, 20+y), outline=1, fill=(255, 0, 0))

        
    disp.image(image, rotation)
    time.sleep(0.05)








