class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # add to the min stack if needed
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()

        # Also make to remove from the minStack if it is present
        if val == self.minStack[-1]:
            min_val = self.minStack.pop()
        

    def top(self) -> int:
        top_val = self.stack[-1]
        return top_val
        

    def getMin(self) -> int:
        min_val = self.minStack[-1]
        return min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()