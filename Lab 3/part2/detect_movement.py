import board
import busio
import adafruit_apds9960.apds9960
import time
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True

detecting = True

while detecting:
    prox = sensor.proximity
    print(prox)
    time.sleep(0.2)
    if prox > 3:
        detecting = False

print('detecting complete, welcome guest')
