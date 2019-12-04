import evdev
import keyboard
import time
import pyautogui

def markings():
    if(keyboard.is_pressed('A')):        
        pyautogui.typewrite('\b' + markedCharacters[1])
        time.sleep(.3)

    #if(keyboard.is_pressed('N')):
    #    keyboard.press_and_release(Key.backspace)
    #    keyboard.type('ñ')
    #    time.sleep(.5)
device = evdev.InputDevice('/dev/input/event2')
markedCharacters = ['á', 'é', 'í', 'ñ', 'ó', 'ú', 'ü']
while True:
    isOn = device.leds(verbose=False)

    if(isOn != [0] and isOn != []):
        markings()