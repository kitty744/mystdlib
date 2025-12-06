_listeners = {}

def on(event_name, func):
    if event_name not in _listeners:
        _listeners[event_name] = []
    _listeners[event_name].append(func)

def off(event_name, func):
    if event_name in _listeners:
        if func in _listeners[event_name]:
            _listeners[event_name].remove(func)

def trigger(event_name, *args, **kwargs):
    if event_name in _listeners:
        for func in _listeners[event_name]:
            func(*args, **kwargs)