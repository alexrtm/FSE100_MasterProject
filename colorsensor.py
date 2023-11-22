# Imports the required libraries.
import time
import board
import adafruit_tcs34725
import busio

class RGB():
    def __init__(self):
        # Create a sensor variable to communicate with your sensor. Uses the I2C interface.
        i2c = board.I2C()
        self.sensor = adafruit_tcs34725.TCS34725(i2c)
        # Set parameters for the sensor
        self.sensor.integration_time = 50
        self.sensor.gain = 4
    
    def color(self):
        # Get and print the color detected
        color = self.sensor.color
        color_rgb = self.sensor.color_rgb_bytes
        return self.determineColor(color_rgb)
        
    def determineColor(self,color_rgb):
        index =  color_rgb.index(max(color_rgb))
        if index == 0:
            return "RED"
        elif index == 1: 
            return "GREEN"
        else:
            return "BLUE"

