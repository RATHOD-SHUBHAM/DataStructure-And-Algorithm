# -----------------------  Brute Force -----------------------

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

 
# -----------------------  Set -----------------------

'''
To check if number is odd, we can replace MOD operation with ABD
>> x % 2 == 1
>> x & 1 == 1

Division operation can be replace with right shift operation
>> x = x // 2
>> x = x >> 1
'''
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countBit(self, x):
        count = 0
        
        while x > 1:
            if x & 1 == 1:
                count += 1
            
            x = x >> 1
        
        if x == 1:
            count += 1
        
        return count
    
if __name__ == '__main__':
    obj = Solution()
    print(obj.countBit(x = 6))


# -----------------------  Turn of rightmost bit -----------------------

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