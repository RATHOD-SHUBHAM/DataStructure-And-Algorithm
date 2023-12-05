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
        
        # When stack is empty - start sorting
        self.sortStack(s, x)
        
        return s
        
    
    def sortStack(self, s, x):
        if not s or s[-1] < x:
            s.append(x)
            return
        else:
            temp = s.pop()
            # When stack is empty - start sorting
            self.sortStack(s, x)
            
            s.append(temp)
            
            return