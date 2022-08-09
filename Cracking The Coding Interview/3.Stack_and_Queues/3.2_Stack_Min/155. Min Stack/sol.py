# Tc: O(1)
# Sc: O(n) # since i am creating a min stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        # add element to stack and also add the min value to min stack
        self.stack.append(val)
        minVal = min(val , self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        # pop element from stack as well as minstack
        self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        # top of stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        # top of min stack
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()