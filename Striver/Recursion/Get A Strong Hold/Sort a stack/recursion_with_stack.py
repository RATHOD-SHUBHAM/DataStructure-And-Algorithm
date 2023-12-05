# Tc: O(n^2) | Sc: O(n)

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        if not s:
            return
    
        # Remove top element
        x = s.pop()
        
        # Recursive call to remove other elements
        self.Sorted(s)
        
        temp_stack = []
        
        # Store greater values in temp stack
        while s and s[-1] > x:
            val = s.pop()
            temp_stack.append(val)
        
        # Place the val in correct position
        s.append(x)
        
        # Put back the greater val
        while temp_stack:
            val = temp_stack.pop()
            s.append(val)