import pyautogui
from PIL import ImageGrab
from pynput import mouse, keyboard  
import numpy as np

x = 183
y = 484
target_color = (119, 216, 119, 255)
running = True  



def on_press(key):
    global running
    try:
        if key.char == 'q':
            print("Q pressed — stopping loop.")
            running = False
            return False 
    except:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:
    pixel_color = ImageGrab.grab(bbox=(x, y, x+1, y+1)).getpixel((0, 0))
    if pixel_color == target_color:
        pyautogui.click(x, y)
        print("Clicked!")
    else:
        print("Waiting...")
       