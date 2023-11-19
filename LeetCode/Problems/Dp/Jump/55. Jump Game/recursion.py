# Tc: O(2^n) | Sc: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        pos = 0
        return self.jump(pos, n, nums)
    
    def jump(self, pos, n , nums):
        # base case
        if pos >= n - 1:
            return True
        
        # idx + val at that index
        farthestJump = pos + nums[pos]
        
        # farthestIdx + 1 - because we have to include the farther index
        for nextPos in range(pos + 1 , farthestJump + 1):
            if self.jump(nextPos, n , nums):
                return True
            
        return False