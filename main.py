import pyautogui
from PIL import ImageGrab
import time
import keyboard

# try:
#     while True:
#         # Get current mouse position
#         x, y = pyautogui.position()

#         # Capture the screen at the mouse location
#         pixel_color = ImageGrab.grab().getpixel((x, y))

#         print(f"Mouse at ({x}, {y}) - Color: {pixel_color}", end='\r')

#         time.sleep(0.1)  # Small delay to reduce CPU usage
# except KeyboardInterrupt:
#     print("\nStopped.")


while True:
    if not keyboard.is_pressed("p"): 
        print("Running Script")
    else:
        print("script stopped")
    if keyboard.is_pressed("q"):
      print("app has been stopped")
      break
