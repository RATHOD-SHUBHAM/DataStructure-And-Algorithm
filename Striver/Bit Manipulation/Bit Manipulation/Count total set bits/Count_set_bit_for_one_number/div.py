class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countBit(self, x):
        count = 0
        
        while x > 1:
            if x % 2 == 1:
                count += 1
            
            x = x // 2
        
        if x == 1:
            count += 1
        
        return count
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.countBit(x = 6))