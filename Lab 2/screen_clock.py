import time
import subprocess
import random
import digitalio
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_apds9960.apds9960
import adafruit_rgb_display.st7789 as st7789
from i2c_button import I2C_Button

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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
progFont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 21)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Button setup code
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()
mainFill = "#FF2D00"

i2c = busio.I2C(board.SCL, board.SDA)
print('I2C devices found:', [hex(n) for n in i2c.scan()])
default_addr = 0x6f
sensor_addr = 0x39
button = I2C_Button(i2c)
button.clear()
button.led_bright=0
button.led_gran = 1
button.led_cycle_ms = 0
button.led_off_ms = 100

oldmin = 10

sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True

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
        fill = mainFill if hour == (currHour % 12) else "#FFFFFF"
        hour = 12 if hour == 0 else hour
        toPrint = str(hour) + " "
        draw.text((x, y), toPrint, font=font, fill=fill)
        x += font.getsize(toPrint)[0]
    
    x = width / 3
    y += font.getsize("sample")[1]
    for ticker in ["AM", "PM"]:
        fill = mainFill if ticker == currTicker else "#FFFFFF"
        draw.text((x, y), ticker, font=font, fill=fill)
        x += width / 3 
    
    x = width / 4
    y += font.getsize("sample")[1]
    for tens in minArrayTens:
        fill = mainFill if currMinTens == tens else "#FFFFFF"
        toPrint = str(tens) + " "
        draw.text((x, y), toPrint, font=font, fill=fill)
        x += font.getsize(toPrint)[0]        

    x = width / 5
    y += font.getsize("sample")[1]
    for ones in minArrayOnes:
        fill = mainFill if currMinOnes == ones else "#FFFFFF"
        toPrint = str(ones) + " "
        draw.text((x, y), toPrint, font=font, fill=fill)
        x += font.getsize(toPrint)[0] 
        if currMinOnes != oldmin:
            print('madeit')
            button.led_bright = 255
            button.led_gran = 1
            button.led_cycle_ms = 500
            button.led_off_ms = 250 
            oldmin = currMinOnes
            time.sleep(1)
        else:
            button.led_bright = 0
            button.led_gran = 1      

    x = 0
    y += font.getsize("sample")[1]
    filled = currSec // 4
    toPrint = '[' + ('=' * filled) + (' ' * (15 - filled)) + ']'
    # toPrint = '|' * currSec
    
    draw.text((x, y), toPrint, font=progFont, fill="#FFFFFF")    

    x = 0
    y += progFont.getsize("sample")[1]
    print(sensor.proximity)
    if sensor.proximity > 15:
        draw.text((x, y), "Clear the area! Object detected.", font=font, fill=mainFill) 
 
    x = 0
    y += font.getsize("sample")[1]
    if not buttonA.value and not buttonB.value:
        draw.text((x, y), "Only press one button!", font=font, fill=mainFill)   
    elif not buttonA.value:
        # Randomize color
        mainFill = '#' + ''.join([hex(random.randint(16, 255))[2:].upper() for i in range(3)])
    elif not buttonB.value:
        # Reset color to normal red
        mainFill = '#FF2D00'

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
