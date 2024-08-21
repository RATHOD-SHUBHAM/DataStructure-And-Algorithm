class MyQueue:
    def __init__(self):
        self.arr = []
    
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.isEmpty():
            return -1
        
        val = self.arr.pop(0)
        
        return val
    
    def peek(self):
        return self.arr[0]