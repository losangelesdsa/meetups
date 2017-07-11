class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        return self._items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self._items.pop()

    def peek(self):
        return self._items[self.size() - 1]

    def size(self):
        return len(self._items)

    def isEmpty(self):
        return self.size() == 0
