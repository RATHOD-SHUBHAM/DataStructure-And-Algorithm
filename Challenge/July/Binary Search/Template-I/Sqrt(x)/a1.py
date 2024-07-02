# Brute
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 1
        
        for i in range(1, x): 
            cur_sqr = i * i

            if cur_sqr <= x:
                ans = i
            else:
                break
        
        return ans
    
# --------------------------------------------------------

# Binary Search
'''
There is a clear division of numbers

For eg:
Sqrt of 24

we dont have to check for number above 5.

so we can eliminate 5 - n, and we will only have to look for number between 1 - 4.

Since 1-3 are too small, we can eliminate that as well

So the only remaining number is 4.
'''
class Solution:
    def mySqrt(self, x: int) -> int:

        low = 1
        high = x

        while low <= high:
            mid = low + (high - low) // 2

            cur_sqr = mid * mid

            if cur_sqr == x:
                return mid
            elif cur_sqr < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high