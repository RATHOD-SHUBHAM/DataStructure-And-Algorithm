# Tc: O(2^n) | Sc: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        pos = 0
        
        return self.game(pos, n , nums)
    
    def game(self, pos, n, nums):
        # base case
        if pos == n - 1:
            return 0
        
        farthestJump = pos + nums[pos]
        min_dist = math.inf
        
        for rechableIdx in range(pos + 1, farthestJump + 1):
            dist = 1 + self.game(rechableIdx, n , nums)
            min_dist = min(min_dist, dist)
        
        return min_dist
     