class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, value):
        self._items.insert(0, value)
        return self._items

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def isEmpty(self):
        return self.size() == 0
