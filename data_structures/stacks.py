class Stacks:
    def __init__(self):
        self._stack = []

    def is_empty(self) -> bool:
        if self._stack is None:
            return True
        else:
            return False

    def pop(self) -> None:
        self._stack.pop()
        
    def push(self, g) -> None:
        self._stack.append(g)

stack = Stacks()
stack.push("test")
stack.push("test3")
print("Initial stack: {}".format(stack._stack))
stack.pop()
print("Stack after popping: {}".format(stack._stack))
print(stack.is_empty())
