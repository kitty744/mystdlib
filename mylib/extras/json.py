import json as _json

def dump(obj, fp, *, indent=None):
    return _json.dump(obj, fp, indent=indent)

def dumps(obj, *, indent=None):
    return _json.dumps(obj, indent=indent)

def load(f):
    return _json.load(f)

def loads(s):
    return _json.loads(s)