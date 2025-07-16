Project, Make a bot that clicks the reflex test button as fast as possible in python then swap to C and build it


Tools I will need

something to find pixle number on the screen 
something to find pixle color 
click()
while 

Steps

write a while loop that is always running unless i hold a button eg. "q"

identify the pixle to target. 

check if this pixle is red.
while the pixle is red do nothing.
once the pixle is green click that pixle

Code to get the pixle 

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
# Reflex_tester_py
