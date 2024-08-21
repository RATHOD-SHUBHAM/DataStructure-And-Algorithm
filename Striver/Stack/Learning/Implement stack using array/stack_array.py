class MyStack:
    
    def __init__(self):
        self.arr=[]
        
    # Function to check if stack is empty.
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.isEmpty():
            return -1
        
        val = self.arr.pop()
        return val
    
    # Function to return the top from stack without removing it.
    def peek(self):
        if self.isEmpty():
            return -1
        
        return self.arr[-1]