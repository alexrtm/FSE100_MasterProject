#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Vibration.py
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

class Vib():
    
    #buzzer is the pin number for output
    def __init__(self, buzzer=11):
        self.buzzer = buzzer
        GPIO.setup(buzzer, GPIO.OUT)
        GPIO.output(buzzer,0)

    def beep(self,x):
        GPIO.output(self.buzzer,1)
        time.sleep(x)
        GPIO.output(self.buzzer,0)
        time.sleep(x)

    def destroy():
        GPIO.output(self.buzzer,0)

