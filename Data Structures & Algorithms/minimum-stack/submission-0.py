class MinStack:
    def __init__(self):
        self.minStack = []
        self.Stack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.minStack.pop()
        self.Stack.pop()
        
    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        
