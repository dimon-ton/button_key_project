import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)


button_pin = board.GP19      # pin to connect button to



# Initializing Button
button = digitalio.DigitalInOut(button_pin)
button.switch_to_input(pull=digitalio.Pull.DOWN)

# if the value equal to False indicate that the button is pressed.


# while True:
#     button_value = button.value
#     print(button_value)
#     time.sleep(0.5)


while True:
    button_value = button.value
    if not button_value:  
        print("the button is pressed")
        keyboard.press(Keycode.F5)
        time.sleep(0.15)
        keyboard.release(Keycode.F5)
  
   
    time.sleep(0.1)
