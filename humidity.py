#!/usr/bin/pyhton

# Tracking the humidity and determining if it is fluctuating or not

# Author: Marius Fjeld Wold

import time
import datetime
import statistics
from collections import deque

#----------------------------- Constants ---------------------------------------
# Standard deviation limit, if the sd of the humidity data set is above this
# limit the humidity is considered to be fluctuating.
SD_LIMIT = 2

# Maximum number readings to store in data set
DATA_SET_LIMIT = 10

#----------------------------- Variables ---------------------------------------
humidity_readings = deque(maxlen=DATA_SET_LIMIT)

#----------------------------- Implementation ----------------------------------
def record_reading(reading):
    # Append reading to back, deques readings automatically
    humidity_readings.append(reading)

def calculate_deviation():
    if len(humidity_readings) is not DATA_SET_LIMIT:
        return 0.0 # Data set not populated
    print 'Standard deviation of data={0:0.1f}%'.format(stdev(humidity))
    return stdev(humidity)

def is_fluctuating():
    if calculate_deviation > SD_LIMIT:
        return True
    return False
