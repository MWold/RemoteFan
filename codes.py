#!/usr/bin/python

import Adafruit_DHT

# Humidity sensor type
DHT_TYPE = Adafruit_DHT.DHT11

# GPIO pin used for reading sensor data
DHT_PIN = 4

# Code for toggling extactor fan on/off
FAN_ON = "1394007"
FAN_OFF = "1394004"

# codesender
SENDER = "./codesend"
