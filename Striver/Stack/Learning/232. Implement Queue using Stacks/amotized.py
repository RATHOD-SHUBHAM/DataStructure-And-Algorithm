'''
Amortized :

When a chucnk of data is transfered at once rather than doing it over and over again.
'''

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = [] 

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        val = self.s2.pop()

        return val

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2[-1]
        

    def empty(self) -> bool:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# -----------------------  Same Solution Different Form ----------------------- 

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = [] 

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        val = self.s2.pop()

        return val

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2[-1]
        

    def empty(self) -> bool:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()