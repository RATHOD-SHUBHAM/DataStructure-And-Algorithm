class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def powerTwo(self, x):
        return (x & (x-1)) == 0
    
    def countOneBit(self, x):
        
        count = 0
        i = 1
        while i <= x:
            if x & i > 0:
                count += 1
            
            i = i << 1
        
        return count
        
    def countSetBits(self,n):
        # code here
        count = 0
        for i in range(1, n + 1):
            if self.powerTwo(i):
                count += 1
            else:
                count += self.countOneBit(i)
        
        # return the count
        return count
    

if __name__ == '__main__':
    obj = Solution()

    print(obj.countSetBits(4))