from gpiozero import LED, Button

led_pins = [8, 7, 16, 20]
leds = [LED(pin) for pin in led_pins]

while True:
    if button.is_pressed:
        for led in leds:
            led.on()
    else:
        for led in leds:
            led.off()