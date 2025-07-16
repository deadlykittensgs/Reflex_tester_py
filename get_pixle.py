import pyautogui
import time
from PIL import ImageGrab


try:
    while True:
        # Get current mouse position
        x, y = pyautogui.position()

        # Capture the screen at the mouse location
        pixel_color = ImageGrab.grab().getpixel((x, y))

        print(f"Mouse at ({x}, {y}) - Color: {pixel_color}", end='\r')

        time.sleep(0.1) 
except KeyboardInterrupt:
    print("\nStopped.")