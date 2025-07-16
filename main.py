import pyautogui
import time
from pynput import keyboard
import mss


# Variables 

x = 183
y = 484
target_color = (119, 216, 119) 
running = True


# Function to kill process
def on_press(key):
    global running
    try:
        if key.char == 'q':
            print("Q pressed — stopping loop.")
            running = False
            return False
    except:
        pass

# start a listener to run function on press  
listener = keyboard.Listener(on_press=on_press)
listener.start()


# run a loop checking a single pixel to see if the color matches the target color
with mss.mss() as sct:
    monitor = {"top": y, "left": x, "width": 1, "height": 1}
    while running:
        img = sct.grab(monitor)
        pixel = img.pixel(0, 0)  # Always (0,0) in a 1x1 image

        if pixel == target_color:
            pyautogui.click(x, y)
            print("Clicked!")
        else:
            print("Waiting...")
            # time.sleep(0.01)  
