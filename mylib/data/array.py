
def append(arr, value):
    arr.append(value)

def remove(arr, value):
    if value in arr:
        arr.remove(value)
        return True
    else:
        return False

def contains(arr, value):
    return value in arr

def length(arr):
    return len(arr)

def insert(arr, index, value):
    arr.insert(index, value)