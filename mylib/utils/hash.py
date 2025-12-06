import hashlib as _hashlib
import random as _random
import string as _string

def md5(text):
    encoded = text.encode("utf-8")
    return _hashlib.md5(encoded).hexdigest()

def sha256(text):
    encoded = text.encode("utf-8")
    return _hashlib.sha256(encoded).hexdigest()

def random_token(length):
    chars = _string.ascii_letters + _string.digits
    return ''.join(_random.choices(chars, k=length))