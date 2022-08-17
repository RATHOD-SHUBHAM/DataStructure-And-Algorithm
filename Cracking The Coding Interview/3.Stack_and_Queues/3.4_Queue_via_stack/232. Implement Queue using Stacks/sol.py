class MyQueue:

    def __init__(self):
        self.s1 = [] # this will have current value
        self.s2 = [] # this will have the value to be popped
        

    # Tc, Sc = O(1)
    def push(self, x: int) -> None:
        self.s1.append(x)
        
    
    # only when i transfer the value from s1 to s2
    # Tc, Sc: O(1), Worst O(n)
    def pop(self) -> int:
        self.peek()
        return self.s2.pop()
        

    # when s2 becomes empty transfer all the value from s1 to s2
    # Tc, Sc: O(1)
    def peek(self) -> int:
        # if s2 is empty add all the value from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
                
                
        return self.s2[-1]
        

    # Tc, Sc: O(1)
    def empty(self) -> bool:
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()