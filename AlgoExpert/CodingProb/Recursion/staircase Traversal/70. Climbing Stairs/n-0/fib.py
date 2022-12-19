class Solution:
    def climbStairs(self, n: int) -> int:
        climb_stair = [1 , 2] # steps to climb stair 1 and stair 2
        
        idx = 3
        
        while idx <= n:
            distinct_climb = climb_stair[0] +climb_stair[1]
            climb_stair[0] = climb_stair[1]
            climb_stair[1] = distinct_climb
            idx += 1
            
        return climb_stair[1] if n > 1 else climb_stair[0]