class MinStack:

    def __init__(self):
        self.stack = []     # All values
        self.minStack = []  # Minimum so far at each index
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Evaluate running minimum value for each index in stack
        val = min(val, self.minStack[-1] if self.minStack else val)

        # Either new value, or existing min
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        # Return the value without removing it
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the value without removing it
        return self.minStack[-1]
        
