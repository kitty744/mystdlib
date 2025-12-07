_events = {}

def on(event, callback):
    if event not in _events:
        _events[event] = []
    _events[event].append(callback)

def off(event, callback):
    if event in _events:
        try:
            _events[event].remove(callback)
        except ValueError:
            pass

def once(event, callback):
    def wrapper(*args, **kwargs):
        off(event, wrapper)
        return callback(*args, **kwargs)
    
    on(event, wrapper)

def emit(event, *args, **kwargs):
    if event not in _events:
        return
    
    for callback in list(_events[event]):
        callback(*args, **kwargs)

def clear(event=None):
    if event is None:
        _events.clear()
    else:
        _events.pop(event, None)