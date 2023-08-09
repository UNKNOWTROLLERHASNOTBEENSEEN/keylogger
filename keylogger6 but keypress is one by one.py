import keyboard
import datetime

def on_key_event(event):
    if event.event_type == 'up':  # Only print for key release events
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} - Key {event.name} released")

keyboard.hook(on_key_event)

keyboard.wait('esc+y')
