memo = {
    1 : 1,
    2 : 2
}

class Solution:
    def climbStairs(self, n: int) -> int:
        
        global memo
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return memo[n]