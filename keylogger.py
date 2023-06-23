import keyboard

def on_key_press(event):
    print(f"Key {event.name} was pressed.")

def on_key_release(event):
    print(f"Key {event.name} was released.")

keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)

keyboard.wait('esc')
