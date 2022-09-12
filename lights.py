"""
This is a simple ws2812b implementation to set ambient lighting for my desk
"""
import board
import neopixel
import RPi.GPIO as GPIO
import argparse

# Use the board internal definition for this
LED_STRIP_OUTPUT_PIN = board.D18  # Physical pin 12

# What GPIO pin is associated with a condition?
DARK_INDICATOR_PIN = 21  # Physical pin 40

# Colors
OFF = (0, 0, 0)


def restricted_float(x):
    """
    Restricts the value to be between 0.0 and 1.0
    :param x: The value to be restricted
    :return: The value if it is within the range
    """
    try:
        x = float(x)
    except ValueError:
        raise argparse.ArgumentTypeError("%r not a floating-point literal" % (x,))

    if x < 0.0 or x > 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]" % (x,))
    return x


def restricted_int(x):
    """
    Restricts the value to be between 0 and 255
    :param x: The value to be restricted
    :return: The value if it is within the range
    """
    try:
        x = int(x)
    except ValueError:
        raise argparse.ArgumentTypeError("%r not an integer" % (x,))

    if x < 0 or x > 255:
        raise argparse.ArgumentTypeError("%r not in range 0-255" % (x,))
    return x


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--num_pixels",
                        type=int,
                        action="store",
                        required=True,
                        dest="num_pixels",
                        help="The number of pixels in the strip")

    parser.add_argument("--brightness",
                        type=restricted_float,
                        action="store",
                        required=False,
                        default=1.0,
                        dest="brightness",
                        help="Set brightness of strip")

    parser.add_argument("--red",
                        type=restricted_int,
                        action="store",
                        required=False,
                        default=0,
                        dest="red",
                        help="Set red pixel value")

    parser.add_argument("--green",
                        type=restricted_int,
                        action="store",
                        required=False,
                        default=0,
                        dest="green",
                        help="Set green pixel value")

    parser.add_argument("--blue",
                        type=restricted_int,
                        action="store",
                        required=False,
                        default=0,
                        dest="blue",
                        help="Set blue pixel value")

    args = parser.parse_args()

    pixels = neopixel.NeoPixel(LED_STRIP_OUTPUT_PIN, args.num_pixels, brightness=args.brightness)

    GPIO.setwarnings(False)

    # Refer pins by their sequence number on the board
    GPIO.setmode(GPIO.BCM)

    # Configure the light sensor
    GPIO.setup(DARK_INDICATOR_PIN, GPIO.IN)

    color = (args.red, args.green, args.blue)

    while True:
        try:
            if GPIO.input(DARK_INDICATOR_PIN):
                pixels.fill(color)
            else:
                pixels.fill(OFF)
        except KeyboardInterrupt:
            pixels.fill(OFF)
            exit()


if __name__ == '__main__':
    main()
