class MyQueue:

    def __init__(self):
        self.s1 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

        if len(self.s1) > 1:
            for i in reversed(range(1, len(self.s1))):
                self.s1[i], self.s1[i-1] = self.s1[i-1] , self.s1[i]


    def pop(self) -> int:
        val = self.s1.pop()

        return val

    def peek(self) -> int:
        top = self.s1[-1]
        return top
        

    def empty(self) -> bool:
        if not self.s1:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()