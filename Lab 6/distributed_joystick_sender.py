import time
import board
import busio
import adafruit_mpr121
import qwiic_joystick
import sys
import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/coolteam'

i2c = busio.I2C(board.SCL, board.SDA)
myJoystick = qwiic_joystick.QwiicJoystick()

print("\nSparkFun qwiic Joystick   Example 1\n")
myJoystick = qwiic_joystick.QwiicJoystick()

if myJoystick.connected == False:
    print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
        file=sys.stderr)

myJoystick.begin()

print("Initialized. Firmware Version: %s" % myJoystick.version)

while True:
    val = "X: %d, Y: %d, Button: %d" % ( \
					myJoystick.horizontal, \
					myJoystick.vertical, \
					myJoystick.button)
    client.publish(topic, val)
    time.sleep(.5)
