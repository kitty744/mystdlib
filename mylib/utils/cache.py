_cache = {}

def set(key, value):
    _cache[key] = value

def get(key, default=None):
    return _cache.get(key, default)

def has(key):
    return key in _cache

def delete(key):
    _cache.pop(key, None)

def clear():
    _cache.clear()