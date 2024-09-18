'''
Get the higherst power of 2

1. Calculate set bit till the highest power of 2

2. Calculate the set bits for MSB

3. Recursively do the same for remaining bits

4. Return the count


Note: 2^x = 1 << x
'''

class Solution:
    def getHighestPower(self, n):
        x = 0
        
        while (1 << x) <= n:
            x += 1
        
        return x - 1
    
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        if n == 0:
            return 0
        
        # Get highest power of 2
        x = self.getHighestPower(n)
        
        # Calculate set bit till the highest power of 2
        setbit_till_power2 = x * (1 << (x - 1))
        
        # Calculate the set bits for MSB
        setbit_for_msb = n - (1 << x) + 1
        
        # Recursively do the same for remaining bits
        remaining_bits = n - (1 << x)
        
        ans = setbit_till_power2 + setbit_for_msb + self.countSetBits(n = remaining_bits)
        
        # return the count
        return ans
    
if __name__ == '__main__':
    ob = Solution()
    print(ob.countSetBits(n = 11))

# Note: sometime in python this solution can give 'negative shift count' Error as this cant handle negative value, use 2 ** x instead