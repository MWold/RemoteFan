#!/usr/bin/pyhton

# Tracking the humidity and determining if it is fluctuating or not

# Author: Marius Fjeld Wold

import time
import datetime
import numpy as np
from collections import deque
class Humidity:
  #----------------------------- Constants ---------------------------------------
  # Standard deviation limit, if the sd of the humidity data set is above this
  # limit the humidity is considered to be fluctuating.
  global SD_LIMIT 

  # Maximum number readings to store in data set
  global DATA_SET_LIMIT

  #----------------------------- Variables ---------------------------------------
  global humidity_readings

  #----------------------------- Implementation ----------------------------------
  def __init__(self):
    self.SD_LIMIT = 2.0
    self.DATA_SET_LIMIT = 10
    
    self.humidity_readings = deque(maxlen=self.DATA_SET_LIMIT)
  
  def record_reading(self, reading):
      # Append reading to back, deques readings automatically
      self.humidity_readings.append(reading)

  def calculate_deviation(self):
      if len(self.humidity_readings) is not self.DATA_SET_LIMIT:
          return 0.0 # Data set not populated
      print 'Standard deviation of data={0:0.1f}%'.format(np.std(self.humidity_readings))
      return np.std(self.humidity_readings)

  def is_fluctuating(self):
      if self.calculate_deviation() > self.SD_LIMIT:
        return True
      return False
