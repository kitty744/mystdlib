class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def peek(self):
        return self.array[-1]

    def is_empty(self):
        return len(self.array) == 0