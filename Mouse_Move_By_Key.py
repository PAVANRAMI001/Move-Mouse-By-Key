import pyautogui as py

py.hotkey('win','d')

from pynput.keyboard import Key, Listener
from pynput.mouse import Controller, Button
import time

# Initialize mouse controller
mouse = Controller()

# Define the step size (distance the mouse will move)
STEP_SIZE = 20

# Initialize variables for space press detection
last_space_press_time = 0
space_press_count = 0
double_press_threshold = 0.5  # Time within which a double press is detected

# Function to handle key press events
def on_press(key):
    global last_space_press_time, space_press_count

    # Get the current mouse position
    x, y = mouse.position

    # Move the mouse based on arrow key inputs
    if key == Key.left:
        mouse.position = (x - STEP_SIZE, y)
    elif key == Key.right:
        mouse.position = (x + STEP_SIZE, y)
    elif key == Key.up:
        mouse.position = (x, y - STEP_SIZE)
    elif key == Key.down:
        mouse.position = (x, y + STEP_SIZE)
    elif key == Key.esc:
        # Stop the listener when 'esc' is pressed
        return False
    elif key == Key.space:
        # Handle space bar for double-click detection
        current_time = time.time()

        if current_time - last_space_press_time <= double_press_threshold:
            space_press_count += 1
            if space_press_count == 2:
                mouse.click(Button.left)  # Perform a click
                space_press_count = 0  # Reset the count after a double click
        else:
            space_press_count = 1
        last_space_press_time = current_time

# Start listening for keyboard events
with Listener(on_press=on_press) as listener:
    listener.join()
