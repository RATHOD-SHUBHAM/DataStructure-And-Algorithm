class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        kth_bit = n & (1 << (k))
        
        return False if kth_bit is 0 else True

# ------------------------------------------------------

class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        n = n >> k
        # print(n)
        
        if n & 1 == 1:
            return True
        else:
            return False