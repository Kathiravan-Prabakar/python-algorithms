class Queues:
    def __init__(self):
        self._queue = []

    def pop(self) -> None:
        self._queue.pop(0)

    def push(self, g) -> None:
        self._queue.append(g)
    
    def is_empty(self):
        if self._queue is None:
            return True
        else:
            return False

queue = Queues()
queue.push("Item 1")
queue.push("Item 2")
queue.push("Item 3")
print("Initial queue: {}".format(''.join(queue._queue)))
queue.pop()
print("Queue after popped: {}".format(''.join(queue._queue)))