from time import strftime, sleep

import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
reset_pin = None
switch = 0 # for button to switch windows

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 17)
timeSize = 54
fontTime = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", timeSize)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

import datetime
from suntime import Sun, SunTimeException

latitude = 40.7
longitude = -74.0

sun = Sun(latitude, longitude)

# Get today's sunrise and sunset in UTC
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
rH = int(today_sr.strftime('%H')) - 5
rM = int(today_sr.strftime('%M'))
sH = int(today_ss.strftime('%H')) - 5
sM = int(today_ss.strftime('%M'))

sunR = "Sun raised at " + (str(rH) + ':' + str(rM))
sunS = "Sun set at " + (str(sH) + ':' + str(sM))

print('Today at New York the sun raised at {} and get down at {} UTC'.
      format((str(rH) + ':' + str(rM)), (str(sH) + ':' + str(sM))))

image2 = Image.open("sun.png")
scaled_width = scaled_height = image2.width // 15
image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)
disp.image(image2)

image3 = Image.open("moon4.png")
scaled_width = scaled_height = image3.width // 150
image3 = image3.resize((scaled_width, scaled_height), Image.BICUBIC)
disp.image(image3)

image4 = Image.open("images/full.png")
scaled_width = scaled_height = image4.width // 6
image4 = image4.resize((scaled_width, scaled_height), Image.BICUBIC)

image5 = Image.open("images/half.png")
scaled_width = scaled_height = image5.width // 6
image5 = image5.resize((scaled_width, scaled_height), Image.BICUBIC)

image6 = Image.open("images/quarter.png")
scaled_width = scaled_height = image6.width // 6
image6 = image6.resize((scaled_width, scaled_height), Image.BICUBIC)

image7 = Image.open("images/empty.png")
scaled_width = scaled_height = image7.width // 6
image7 = image7.resize((scaled_width, scaled_height), Image.BICUBIC)

while True:
    if not buttonA.value:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        disp.image(image, rotation)
        switch += 1
    if not buttonB.value:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
        disp.image(image, rotation)
        switch -= 1

    case = 1
    if case == 0:
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        date = strftime("%m/%d/%Y")
        # time = strftime("%H:%M:%S")
        nowH = strftime("%H")
        nowM = strftime("%M")
        nowS = strftime("%S")
        time = nowH + ":" + nowM + ":" + nowS


        print (date+" "+time, end="", flush=True)
        print("\r", end="", flush=True)
        date = "Date: " + date

        y = top
        draw.text((x, y), date, font=font, fill="#FFFFFF")

        y += font.getsize(date)[1] + 14
        nowH = int(nowH)
        if nowH in range(rH, 11): # morning
            draw.text((x, y), time, font=fontTime, fill="#f5fed5")
        elif nowH in range(11, 13): # noon
            draw.text((x, y), time, font=fontTime, fill="#e8bf4e")
        elif nowH in range(13, 15): # afternoon
            draw.text((x, y), time, font=fontTime, fill="#e69d3e")
        elif nowH in range(15, sH): # afternoon
            draw.text((x, y), time, font=fontTime, fill="#dc783e")
        elif nowH in range(sH, 23): # night
            draw.text((x, y), time, font=fontTime, fill="#a1cff7")
        elif nowH in range(0, rH) or nowH >= 23: # midnight
            draw.text((x, y), time, font=fontTime, fill="#3b5278")
        # y += font.getsize(time)[1]
        y += timeSize + 14
        draw.text((x, y), sunR, font=font, fill="#FF78FF")

        y += font.getsize(sunR)[1]
        draw.text((x, y), sunS, font=font, fill="#FCF80F")

        if nowH in range(rH, sH):
            disp.image(image2)
        else:
            disp.image(image3)
            disp.image(image, rotation)
    if case == 1:
        disp.image(image4, rotation)
    if case == 2:
        disp.image(image5, rotation)
    if case == 3:
        disp.image(image6, rotation)
    if case == 4:
        disp.image(image7, rotation)
    sleep(0.1)
