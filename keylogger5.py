import keyboard
import datetime

def on_key_event(event):
    event_type = 'pressed' if event.event_type == 'down' else 'released'
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - Key {event.name} {event_type}")

keyboard.hook(on_key_event)

keyboard.wait('esc+y')
