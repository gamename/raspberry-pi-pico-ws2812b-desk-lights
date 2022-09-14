"""
This is a simple config to light a strip of ws2812b LEDs strategically located behind my desk.
"""
import time
from neopixel import NeoPixel
from machine import Pin

# How many pixels do we have?
PIXEL_COUNT = 172

# Which pin controls the light strip?
PIXEL_PIN = Pin(0)

# Define the color we want to use for the light strip
BLUE = (0, 0, 255)

OFF = (0, 0, 0)

pixels = NeoPixel(PIXEL_PIN, PIXEL_COUNT)

pixels.fill(OFF)
pixels.write()

while True:
    pixels.fill(BLUE)
    pixels.write()
