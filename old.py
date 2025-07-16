import pyautogui 
from PIL import ImageGrab
from pynput import keyboard  



# Choose what pixles you want to watch 
x = 183
y = 484
target_color = (119, 216, 119, 255)
running = True  


def on_press(key):
    # "global" allows you to access the variable "running" listed above. 
    # Without this I would need to put it in the function
    global running
    # try catch block syntax. Try to run code and if happens
    # run code except = if it fails run code. prints error
    try:
        if key.char == 'q':
            print("Q pressed — stopping loop.")
            running = False
            return 
    except Exception as e:
        print("Exception occurred: {e}")
        
       

listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:
    pixel_color = ImageGrab.grab(bbox=(x, y, x+1, y+1)).getpixel((0, 0))
    if pixel_color == target_color:
        pyautogui.click(x, y)
        print("Clicked!")
    else:
        print("Waiting...")
       