# Tc: O(n^2) | Sc: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        pos = 0
        memo = [None] * n
        return self.jump(pos, n, memo, nums)
    
    def jump(self, pos, n , memo, nums):
        # base case
        if pos >= n - 1:
            return True
        
        if memo[pos]:
            return memo[pos]
        
        # idx + val at that index
        farthestJump = pos + nums[pos]
        
        # farthestIdx + 1 - because we have to include the farther index
        for nextPos in range(pos + 1 , farthestJump + 1):
            if self.jump(nextPos, n , memo, nums):
                memo[pos] = True
            else:
                memo[pos] = False
            
        return memo[pos]