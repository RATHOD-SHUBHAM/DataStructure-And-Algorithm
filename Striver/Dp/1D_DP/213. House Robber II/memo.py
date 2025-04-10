class Solution:
    def recursion(self, dp, n, nums):
        if n < 0:
            return 0
        
        if dp[n] != -1:
            return dp[n]
        
        pick = nums[n] + self.recursion(dp, n-2, nums) # Cannot moce to adjacent house
        not_pick = 0 + self.recursion(dp, n-1, nums) # If we dont pick current house, we can move to adjacent house

        dp[n] = max(pick, not_pick)
        return dp[n]

    def house_robber_1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        return self.recursion(dp, n-1, nums)
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        num_1 = nums[0 : n-1]
        num_2 = nums[1: n]

        return max(self.house_robber_1(num_1), self.house_robber_1(num_2))
        