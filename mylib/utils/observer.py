_observers = {}
_values = {}

def watch(name, callback):
    if name not in _observers:
        _observers[name] = []
    _observers[name].append(callback)

def unwatch(name, callback):
    if name in _observers:
        if callback in _observers[name]:
            _observers[name].remove(callback)

def set_value(name, new_value):
    old_value = _values.get(name)
    _values[name] = new_value

    if old_value != new_value:
        for callback in _observers.get(name, []):
            callback(new_value)

def get_value(name):
    return _values.get(name)