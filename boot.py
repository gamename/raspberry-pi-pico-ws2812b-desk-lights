"""
This is a simple config to light a strip of ws2812b LEDs strategically located behind my desk.
"""
from neopixel import NeoPixel
from machine import Pin
import time

# How many pixels do we have?
PIXEL_COUNT = 172

# How bright do we want to display?
BRIGHTNESS = 0.5  # 50% brightness

# How long between tests should we wait?
SLEEP_SECONDS = 60

# Which pin controls the light strip?
WS2812_CONTROL_PIN = Pin(0)
LIGHT_SENSOR_PIN = 1

# Define the color we want to use for the light strip
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

pixels = NeoPixel(WS2812_CONTROL_PIN, PIXEL_COUNT)
dark = Pin(LIGHT_SENSOR_PIN, Pin.IN, Pin.PULL_DOWN)

pixels.brightness = BRIGHTNESS

while True:
    if dark.value():
        pixels.fill(BLUE)
        pixels.write()
    else:
        pixels.fill(OFF)
        pixels.write()
    time.sleep(SLEEP_SECONDS)
