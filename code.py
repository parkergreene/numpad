import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

pause_time = 0.1

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
keyboard = Keyboard(usb_hid.devices)

btn1_pin = board.GP0
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2_pin = board.GP1
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3_pin = board.GP2
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4_pin = board.GP3
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5_pin = board.GP4
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6_pin = board.GP5
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7_pin = board.GP6
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8_pin = board.GP7
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9_pin = board.GP8
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10_pin = board.GP9
btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11_pin = board.GP10
btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12_pin = board.GP11
btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

btn13_pin = board.GP12
btn13 = digitalio.DigitalInOut(btn13_pin)
btn13.direction = digitalio.Direction.INPUT
btn13.pull = digitalio.Pull.DOWN

btn14_pin = board.GP13
btn14 = digitalio.DigitalInOut(btn14_pin)
btn14.direction = digitalio.Direction.INPUT
btn14.pull = digitalio.Pull.DOWN

btn15_pin = board.GP14
btn15 = digitalio.DigitalInOut(btn15_pin)
btn15.direction = digitalio.Direction.INPUT
btn15.pull = digitalio.Pull.DOWN

btn16_pin = board.GP15
btn16 = digitalio.DigitalInOut(btn16_pin)
btn16.direction = digitalio.Direction.INPUT
btn16.pull = digitalio.Pull.DOWN

btn17_pin = board.GP16
btn17 = digitalio.DigitalInOut(btn17_pin)
btn17.direction = digitalio.Direction.INPUT
btn17.pull = digitalio.Pull.DOWN


while True:
    if btn1.value:
        button = Keycode.KEYPAD_ONE
        print("1 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)
    
    if btn2.value:
        button = Keycode.KEYPAD_TWO
        print("2 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)
    
    if btn3.value:
        button = Keycode.KEYPAD_THREE
        print("3 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)
    
    if btn4.value:
        button = Keycode.KEYPAD_FOUR
        print("4 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn5.value:
        button = Keycode.KEYPAD_FIVE
        print("5 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn6.value:
        button = Keycode.KEYPAD_SIX
        print("6 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn7.value:
        button = Keycode.KEYPAD_SEVEN
        print("7 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn8.value:
        button = Keycode.KEYPAD_EIGHT
        print("8 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn9.value:
        button = Keycode.KEYPAD_NINE
        print("9 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn10.value:
        button = Keycode.KEYPAD_NUMLOCK
        print("Numlock Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn11.value:
        button = Keycode.KEYPAD_FORWARD_SLASH
        print("/ Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn12.value:
        button = Keycode.KEYPAD_ASTERISK
        print("* Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn13.value:
        button = Keycode.KEYPAD_PERIOD
        print(". Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn14.value:
        button = Keycode.KEYPAD_MINUS
        print("- Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn15.value:
        button = Keycode.KEYPAD_ZERO
        print("0 Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn16.value:
        button = Keycode.KEYPAD_ENTER
        print("Enter Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)

    if btn17.value:
        button = Keycode.KEYPAD_PLUS
        print("+ Pressed")
        keyboard.press(button)
        led.value = True
        time.sleep(pause_time)
        keyboard.release(button)
        led.value = False
    #time.sleep(pause_time)