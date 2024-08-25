# 2 Queue
from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        val = self.q1.popleft()
        
        # Swap the queue
        self.q1 , self.q2 = self.q2 , self.q1
        
        return val
        

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top_ele = self.q1[0]

        # Swap the stack
        self.q2.append(self.q1.popleft())
        self.q1 , self.q2 = self.q2 , self.q1

        return top_ele

    def empty(self) -> bool:
        if not self.q1 and not self.q2:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()