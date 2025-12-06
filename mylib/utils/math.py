def max(a, b):
    if a > b:
        return a
    else:
        return b

def min(a, b):
    if a < b:
        return a
    else:
        return b

def abs(x):
    if x < 0:
        return -x
    else:
        return x

def sum(arr):
    total = 0
    for item in arr:
        total += item
    return total

def avg(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)