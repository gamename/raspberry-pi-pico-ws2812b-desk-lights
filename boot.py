"""
This is a simple config to light a strip of ws2812b LEDs strategically located behind my desk.
"""
import time
from neopixel import NeoPixel
from machine import Pin

# How many pixels do we have?
PIXEL_COUNT = 172

# How bright do we want to display?
BRIGHTNESS = 0.5

# Which pin controls the light strip?
PIXEL_PIN = Pin(0)
DARKNESS_DETECTION_PIN = 1

# Define the color we want to use for the light strip
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

pixels = NeoPixel(PIXEL_PIN, PIXEL_COUNT)
dark = Pin(DARKNESS_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)

pixels.brightness = BRIGHTNESS

pixels.fill(OFF)
pixels.write()

while True:
    if dark.value():
        pixels.fill(BLUE)
        pixels.write()
    else:
        pixels.fill(OFF)
        pixels.write()
