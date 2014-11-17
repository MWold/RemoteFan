#!/usr/bin/pyhton

# Tracking the humidity and determining if it is fluctuating or not

# Author: Marius Fjeld Wold

import time
import datetime
import statistics

#----------------------------- Constants ---------------------------------------
# dh at which humidity is considered to be stable
STABLE_LEVEL = 20

# dh at which humidity is considered to be changing
CHANGING_LEVEL = 50

#----------------------------- Variables ---------------------------------------
previous_reading = 0.0

humidity_change = 0.0

standard_deviation = 0.0

humidity_readings = []

# Use some sort of push/pop combination to remove oldest value when new value is inserted

#----------------------------- Attributes --------------------------------------
def get_changing_level():
    return CHANGING_LEVEL

def get_stable_level():
    return STABLE_LEVEL

#----------------------------- Implementation ----------------------------------
