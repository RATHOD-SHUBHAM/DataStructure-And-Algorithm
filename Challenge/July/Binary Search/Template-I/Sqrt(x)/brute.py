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