# MLH Hack From The Past hackathon
# Project: Time Capsule
# Author: Advik Singhania

import time
import board
import digitalio
import pulseio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# The keyboard object!
time.sleep(2)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

button = digitalio.DigitalInOut(board.A6)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

space = digitalio.DigitalInOut(board.A4)
space.direction = digitalio.Direction.INPUT
space.pull = digitalio.Pull.DOWN

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

buzzer = pulseio.PWMOut(board.D5, variable_frequency=True)
# buzzer.frequency = 3000
OFF = 0
ON = 2**15

print('Waiting for key pin...')

while True:
    if button.value:
        buzzer.frequency = 3000
        time.sleep(0.25)
        if not button.value:
            buzzer.duty_cycle = ON
            time.sleep(0.15)
            print('.', end='')
            keyboard_layout.write('.')
            buzzer.duty_cycle = OFF
        else:
            buzzer.duty_cycle = ON
            time.sleep(0.35)
            print('_', end='')
            keyboard_layout.write('-')
            buzzer.duty_cycle = OFF
    elif space.value:
        buzzer.frequency = 3000
        buzzer.duty_cycle = ON
        time.sleep(0.05)
        buzzer.duty_cycle = OFF
        time.sleep(0.05)
        print(' ', end='')
        keyboard_layout.write(' ')
        buzzer.duty_cycle = ON
        time.sleep(0.05)
        buzzer.duty_cycle = OFF
        time.sleep(0.05)
