from gpiozero import LED, Button
from time import sleep
from signal import pause

led_pins=[8,7,16,20]
leds=[LED(pin) for pin in led_pins]
button=Button(21)

def domino4():
    for led in leds:
        led.on()
        sleep(1)
        led.off()

button.when_pressed = domino4

pause()