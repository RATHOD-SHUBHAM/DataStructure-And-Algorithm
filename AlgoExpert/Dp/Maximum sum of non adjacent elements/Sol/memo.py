# Tc: O(n) | Sc: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [None] * n
        return self.recursion(n - 1, memo, nums)
        
        
    def recursion(self, idx, memo, nums):
        # base case
        if memo[idx] != None:
            return memo[idx]
        
        if idx < 0:
            return 0
        
        if idx == 0:
            return nums[0]
        
        pick = nums[idx] + self.recursion(idx - 2, memo, nums)
        dontPick = 0 + self.recursion(idx - 1, memo, nums)
        
        memo[idx] = max(pick, dontPick)
        
        return memo[idx]
        