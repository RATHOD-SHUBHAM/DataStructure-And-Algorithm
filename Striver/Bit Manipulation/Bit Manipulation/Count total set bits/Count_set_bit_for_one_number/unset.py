# Kernighan’s bit count algorithm

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countBit(self, x):
        count = 0
        
        while x != 0:
            x = x & (x-1) # Turn of rightmost bit
            count += 1
        
        return count
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.countBit(x = 6))