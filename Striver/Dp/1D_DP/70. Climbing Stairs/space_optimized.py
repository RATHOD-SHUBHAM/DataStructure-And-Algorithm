class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        p_prev = 1
        prev = 2
        
        for i in range(3, n+1):
            cur_ways = prev + p_prev
            p_prev = prev
            prev = cur_ways
        
        return cur_ways