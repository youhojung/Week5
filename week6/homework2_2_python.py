from gpiozero import LED, Button
from signal import pause

led_pins=[8,7,16,20]
leds=[LED(pin) for pin in led_pins]
button=Button(25)

leds_on = [False]

def toggle_leds():
    leds_on[0] = not leds_on[0]
    for led in leds:
        if leds_on[0]:
            led.on()
        else:
            led.off()

button.when_pressed = toggle_leds

pause()