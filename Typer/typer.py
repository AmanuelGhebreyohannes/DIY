import sys
from pynput import mouse
from pynput import keyboard
import time

def on_click(x, y, button, pressed):
    
    if button == mouse.Button.left and pressed:
        print('clicked')
        read_file_and_press_keys(filename)
        return True  # Stop listener to indicate double-click event
    return False

def on_press(key):
    pass  # Placeholder function to satisfy pynput.Listener requirements

def read_file_and_press_keys(filename):
    # Read the content of the file
    with open(filename, 'r') as file:
        content = file.read()

    # Create an instance of the Controller object
    controller = keyboard.Controller()

    # Initialize cursor position
    cursor_position = (0, 0)

    # Simulate keypresses based on the file content
    for char in content:
        if char == '\n':
            # Simulate Enter key
            controller.press(keyboard.Key.enter)
            controller.release(keyboard.Key.enter)
            # Reset cursor position to left corner
            cursor_position = (0, 0)
        elif char == '\t':
            cursor_position = (0, 0)
            # Simulate Tab keyrtle.fd(45)
            controller.press(keyboard.Key.tab)
            controller.release(keyboard.Key.tab)
            # Adjust cursor position for tab
            
        else:
            # Simulate regular keypress
            controller.press(char)
            controller.release(char)
            # Adjust cursor position
            #cursor_position = (cursor_position[0] + 1, cursor_position[1])
            cursor_position = (0, 0)
        time.sleep(0.075)  # Adjust the delay as needed

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # Start listening for mouse events
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    # Read the file and press keys upon double-click event
    #read_file_and_press_keys(filename)
