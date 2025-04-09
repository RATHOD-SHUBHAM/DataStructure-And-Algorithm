class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        return self.recursion(dp, n-1, nums)
    
    def recursion(self, dp, n, nums):
        if n < 0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        pick = nums[n] + self.recursion(dp, n-2, nums) # Cannot moce to adjacent house
        not_pick = 0 + self.recursion(dp, n-1, nums) # If we dont pick current house, we can move to adjacent house

        dp[n] = max(pick, not_pick)
        return dp[n]