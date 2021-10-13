import digitalio
import board
from time import perf_counter
import sys
import os

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors

# The display uses a communication protocol called SPI.
# SPI will not be covered in depth in this course.
# you can read more https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)


# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

detecting_doorbell = True
while detecting_doorbell:
    print('detecting doorbell')
    if not buttonB.value:
        print('doorbell detected, begin door open detection')
        detecting_doorbell = False

detecting_dooropen = True
time_threshold = 3
currTime = perf_counter()
while detecting_dooropen and (perf_counter() - currTime < time_threshold):
    print(perf_counter() - currTime)
    if not buttonA.value:
        print('door opened!')
        detecting_dooropen = False

if detecting_dooropen:
    print('beginning recording')
    os.system("./record.sh")
else:
    print('Door open, ending wizard')
