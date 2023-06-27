import keyboard

def on_key_event(event):
    with open("keyrecord.txt", "a") as file:
        file.write(f"Key {event.name} {'pressed' if event.event_type == 'down' else 'released'}\n")

keyboard.on_press(on_key_event)
keyboard.on_release(on_key_event)

keyboard.wait('esc')
