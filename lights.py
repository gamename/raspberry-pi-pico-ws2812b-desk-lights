"""
"""
import board
import neopixel
import RPi.GPIO as GPIO

# How many pixels are in the WS2812b strip?
MAX_PIXELS = 102

# How bright should the LEDs be?
BRIGHTNESS = 0.20  # 20%

# Use the board internal definition for this
LED_STRIP_OUTPUT_PIN = board.D18  # Physical pin 12

# What GPIO pin is associated with a condition?
DARK_INDICATOR_PIN = 21  # Physical pin 40

# Colors
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(LED_STRIP_OUTPUT_PIN, MAX_PIXELS, brightness=BRIGHTNESS)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Configure the light sensor
GPIO.setup(DARK_INDICATOR_PIN, GPIO.IN)

while True:
    try:
        if GPIO.input(DARK_INDICATOR_PIN):
            pixels.fill(BLUE)
        else:
            pixels.fill(OFF)
    except KeyboardInterrupt:
        pixels.fill(OFF)
        exit()
