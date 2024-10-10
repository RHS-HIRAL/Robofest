"""
Test script to toggle rpi gpio pins

based on https://www.instructables.com/Raspberry-Pi-Python-scripting-the-GPIO/

first need to `sudo apt-get install python3-rpi.gpio` on the rpi

If you get any weird errors like "RuntimeError: Not running on a RPi!", try 
restarting the pi. This worked for me, even running with ubuntu

note your user needs to be in dialout group, see https://github.com/gpiozero/gpiozero/issues/837

some docs on the api: https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api
"""

import RPi.GPIO as gpio
import time

# on pcb rev 2.0, these are the gpio pins connected to leds on the brain board
valid_gpio_nums = [25, 26, 5, 6]

gpio.setwarnings(False)

# there are two modes, BCM and BOARD
gpio.setmode(gpio.BCM)

# flash each of the LEDs, in turn
for tindx in range(4):
    for indx in range(4):
        print(indx)
        gpio_num = valid_gpio_nums[indx]
        gpio.setup(gpio_num, gpio.OUT)
        gpio.output(gpio_num, True)
        time.sleep(1)
        gpio.output(gpio_num, False)
        time.sleep(1)

gpio.cleanup()