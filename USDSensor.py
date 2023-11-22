#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  USDSensor.py
#  
#  Copyright 2023  <pi@pi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

class USD():
    # crit_range is the distance within which the sensor activates
    # trig is the GPIO pin number for input
    # echo is the GPIO pin number for output
    def __init__(self,crit_range,trig=11,echo=12):
        self.TRIG = trig
        self.ECHO = echo
        self.CRITICAL_RANGE = crit_range # upper limit for distance sensor
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

    def distance(self):
        GPIO.output(self.TRIG, 0)
        time.sleep(0.000002)

        GPIO.output(self.TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, 0)

        while GPIO.input(self.ECHO) == 0:
            a = 0
        time1 = time.time()
        
        while GPIO.input(self.ECHO) == 1:
            a = 1
        time2 = time.time()
        
        during = time2 - time1
        return during * 340 / 2 * 100
    
