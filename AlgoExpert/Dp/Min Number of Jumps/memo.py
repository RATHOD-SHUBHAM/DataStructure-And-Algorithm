# Tc: O(n^2) | Sc: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        pos = 0
        
        memo = [None] * n
        return self.game(pos, n , memo, nums)
    
    def game(self, pos, n, memo, nums):
        # base case
        if pos == n - 1:
            return 0
        
        if memo[pos]:
            return memo[pos]
        
        farthestJump = pos + nums[pos]
        min_dist = math.inf
        
        for rechableIdx in range(pos + 1, farthestJump + 1):
            dist = 1 + self.game(rechableIdx, n , memo, nums)
            min_dist = min(min_dist, dist)
        
        memo[pos] = min_dist
        return memo[pos]