#!/usr/bin/python

import Adafruit_DHT

# Humidity sensor type
DHT_TYPE = Adafruit_DHT.DHT11

# GPIO pin used for reading sensor data
DHT_PIN = 4

# Code for toggling extactor fan on/off
FAN_ON = "sudo ./home/pi/git/433Utils/RPi_utils/codesend 1394007"
FAN_OFF = "sudo ./home/pi/git/433Utils/RPi_utils/codesend 1394004"

# Where is the 433Utils sender program
SENDER = ""
