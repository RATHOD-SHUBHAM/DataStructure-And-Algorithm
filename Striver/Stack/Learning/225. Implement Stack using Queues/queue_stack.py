class MyStack:

    def __init__(self):
        self.myQueue = []
        

    def push(self, x: int) -> None:
        self.myQueue.append(x)

        n = len(self.myQueue)

        # Reverse the Stack
        for _ in range(n - 1):
            val = self.pop()
            self.myQueue.append(val)

        

    def pop(self) -> int:
        if self.empty():
            return 
        
        val = self.myQueue.pop(0)

        return val
        

    def top(self) -> int:
        if self.empty():
            return 
        
        return self.myQueue[0]
        

    def empty(self) -> bool:
        if len(self.myQueue) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()