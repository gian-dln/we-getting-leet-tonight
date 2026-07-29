class MinStack:

    def __init__(self): 
        self.stack = []
        self.minStack = []


    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)
    

    def pop(self) -> None:
        if self.stack: #if stack is not empty
            value = self.stack.pop()
            if value == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(1)
# obj.push(14)
# obj.push(1)
# obj.push(-1)
# obj.push(3)
# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3)
# print(param_4)