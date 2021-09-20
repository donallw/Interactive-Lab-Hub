import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 17)
progFont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 21)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
#TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    currHour = int(time.strftime("%H"))
    currMinTens = int(time.strftime("%M")) // 10
    currMinOnes = int(time.strftime("%M")) % 10
    currSec = int(time.strftime("%S"))

    hourArray = [i for i in range(12)]
    minArrayTens = [i for i in range(6)]
    minArrayOnes = [i for i in range(10)]

    currTicker = "AM" if currHour < 12 else "PM"
    
    y = top
    x = 0
    for hour in hourArray:
        fill = "#FF2D00" if hour == (currHour % 12) else "#FFFFFF"
        hour = 12 if hour == 0 else hour
        toPrint = str(hour) + " "
        draw.text((x, y), toPrint, font=font, fill=fill)
        x += font.getsize(toPrint)[0]
    
    x = width / 3
    y += font.getsize("sample")[1]
    for ticker in ["AM", "PM"]:
        fill = "#FF2D00" if ticker == currTicker else "#FFFFFF"
        draw.text((x, y), ticker, font=font, fill=fill)
        x += width / 3 
    
    x = width / 4
    y += font.getsize("sample")[1]
    for tens in minArrayTens:
        fill = "#FF2D00" if currMinTens == tens else "#FFFFFF"
        toPrint = str(tens) + " "
        draw.text((x, y), toPrint, font=font, fill=fill)
        x += font.getsize(toPrint)[0]        

    x = width / 5
    y += font.getsize("sample")[1]
    for ones in minArrayOnes:
        fill = "#FF2D00" if currMinOnes == ones else "#FFFFFF"
        toPrint = str(ones) + " "
        draw.text((x, y), toPrint, font=font, fill=fill)
        x += font.getsize(toPrint)[0]        

    x = 0
    y += font.getsize("sample")[1]
    filled = currSec // 4
    toPrint = '[' + ('=' * filled) + (' ' * (15 - filled)) + ']'
    # toPrint = '|' * currSec
    
    draw.text((x, y), toPrint, font=progFont, fill="#FFFFFF")    
      
    
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
