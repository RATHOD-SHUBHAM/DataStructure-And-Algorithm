class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        kth_bit = n & (1 << (k))
        
        return False if kth_bit is 0 else True