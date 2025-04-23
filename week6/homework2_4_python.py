from gpiozero import LED, Button
from time import sleep
from signal import pause

led_pins=[8,7,16,20]
leds=[LED(pin) for pin in led_pins]
button=Button(25, bounce_time=0.1)
j = 0

def count16():
    global j
    j=(j+1)%16
    for i in range(4):
        if (j >> i) & 1 :
            leds[i].on()
        else:
            leds[i].off()

button.when_pressed = count16

pause()