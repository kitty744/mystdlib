class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, value):
        self.array.append(value)

    def dequeue(self):
        return self.array.pop(0)

    def peek(self):
        return self.array[0]

    def is_empty(self):
        return len(self.array) == 0