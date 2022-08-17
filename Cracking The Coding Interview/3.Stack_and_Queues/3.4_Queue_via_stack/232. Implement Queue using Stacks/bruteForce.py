class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    # every time we add a value to s1.
    # copy all the content from s1 to s2
    # add new value to empty s1
    # then copy back all the content from s2 to s1
    
    # Tc,Sc: O(n)
    def push(self, x: int) -> None:
        # if there are element in s1, make a copy in s2
        while self.s1:
            self.s2.append(self.s1.pop())
            
        # add value to s1
        self.s1.append(x)
        
        # copy back all the value from s2 to s1
        while self.s2:
            self.s1.append(self.s2.pop())
            
        

    # Tc, Sc: O(1)
    def pop(self) -> int:
        return self.s1.pop()
        

    # Tc, Sc: O(1)
    def peek(self) -> int:
        return self.s1[-1]
        

    # Tc, Sc: O(1)
    def empty(self) -> bool:
        return not self.s1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()