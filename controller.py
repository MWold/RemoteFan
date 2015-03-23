#!/usr/bin/python

# Simple program for controlling a bathroom extractor fan through the use of
# togleable power outlets over the popular 433MHz frequency.

# Author: Marius Fjeld Wold

# Based on code from Adafruit Industries
# See below for details

#----------------------------- BEGIN DETAILS -----------------------------------

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#---------------------------- END DETAILS --------------------------------------

import sys
import time
import datetime
import subprocess

import Adafruit_DHT

import codes
from humidity import Humidity

#----------------------------- Constants ---------------------------------------
# Sampling frequency (in seconds)
FREQUENCY_SECONDS = 15

#----------------------------- Variables ---------------------------------------

# Is the fan turned on?
fan_is_on = False

hum = Humidity() 
hum.__init__()

#----------------------------- Functionality -----------------------------------

# Toggle fan
def toggle_fan(state):
    if state:
        subprocess.call(['sudo',codes.SENDER,codes.FAN_ON])
    else:
        subprocess.call(['sudo',codes.SENDER,codes.FAN_OFF])

while True:
  # Read sensor
  humidity_reading, temp = Adafruit_DHT.read(codes.DHT_TYPE, codes.DHT_PIN)

  # If we can't get a reading we skip this one, sometimes we can't get a
  # measurement because reasons.
  if humidity_reading is None or temp is None:
    time.sleep(2)
    continue

  # Printing to standard output for testing purposes.
  print 'Humidity={0:0.1f}%'.format(humidity_reading)

  # Record the reading
  hum.record_reading(humidity_reading)

  if humidity_reading >= 40.0 and hum.is_fluctuating() and not fan_is_on:
    print 'Turning fan on!'
    fan_is_on = True

  if humidity_reading < 40.0 and not hum.is_fluctuating() and fan_is_on:
    print 'Turning fan off!'
    fan_is_on = False

  toggle_fan(fan_is_on)

  # Wait until it's time to read the sensor again
  time.sleep(FREQUENCY_SECONDS)
