# catch is to understand that every n steps is sum of n-1 and n-2 step
# eg step 3 = step 1 + step 2

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        