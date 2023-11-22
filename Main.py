#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Main.py
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

import RPi.GPIO as GPIO
import time
import board
import adafruit_tcs34725
import USDSensor as usd
import colorsensor as rgb
import Vibration as vib
import subprocess

crit_range = 10 # the upper limit of the USD sensor's range in cm 

class Module():
    def __init__(self, distance_sensor, rgb_sensor,buzzer):
        self.distance_sensor = distance_sensor
        self.rgb_sensor = rgb_sensor
        self.buzzer = buzzer
        
    def activate(self):
        dis = self.distance_sensor.distance()
        print(self.distance_sensor.CRITICAL_RANGE, dis)
        if dis <= self.distance_sensor.CRITICAL_RANGE:
            self.buzzer.beep(1)
            print (dis, 'cm')
            print ('')
            if self.rgb_sensor != None:
                c = self.rgb_sensor.color()
                print(
                "RGB color:   ", c
                )
                subprocess.call(("espeak \"The color is " + c + "\" 2>/dev/null").split(" "))
                print('')
        #time.sleep(0.3)
        


def loop(modules):
    while True:
        modules[0].activate()
        modules[1].activate()
        modules[2].activate()
        

if __name__ == '__main__':
    distance_sensor1 = usd.USD(crit_range,20,21)
    rgb_sensor = rgb.RGB()
    buzzer1 = vib.Vib(24)
    module_center = Module(distance_sensor1,rgb_sensor,buzzer1)
    
    distance_sensor2 = usd.USD(crit_range,5,6)
    buzzer2 = vib.Vib(17)
    module_left = Module(distance_sensor2,None,buzzer2)
    
    distance_sensor3 = usd.USD(crit_range,19,26)
    buzzer3 = vib.Vib(27)
    module_right = Module(distance_sensor3,None,buzzer3)
    
    modules = [module_center,module_left,module_right]
    
    try: 
        loop(modules)
    except KeyboardInterrupt: 
        GPIO.cleanup()
