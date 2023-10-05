class StackMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.stack:
            return None
        self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

# Test
stack = StackMin()
stack.push(5)
print(stack.min())  # 5
stack.push(6)
print(stack.min())  # 5
stack.push(3)
print(stack.min())  # 3
stack.push(7)
print(stack.min())  # 3
stack.pop()
print(stack.min())  # 3
stack.pop()
print(stack.min())  # 5
