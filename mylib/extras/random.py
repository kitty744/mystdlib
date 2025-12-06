import random as _random

def randint(a, b):
    return _random.randint(a, b)

def choice(seq):
    return _random.choice(seq)

def shuffle(seq):
    _random.shuffle(seq)
    return seq

def random():
    return _random.random()