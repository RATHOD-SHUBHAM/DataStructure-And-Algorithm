class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)
        

    def popMax(self) -> int:
        
        maxVal = self.peekMax()
        
        # iterate from back as stack is FIFO
        for i in reversed(range(0 , len(self.stack))):
            if self.stack[i] == maxVal:
                del(self.stack[i])
                break
                
        return maxVal
            
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()