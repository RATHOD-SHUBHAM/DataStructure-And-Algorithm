class Solution:
    def house_robber_1(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [-1] * n
        dp[0] = nums[0]

        for i in range(1, n):
            pick = nums[i] + (dp[i-2] if i-2 >= 0 else 0) # the brackets are important
            not_pick = 0 + (dp[i-1] if i-1 >= 0 else 0)

            dp[i] = max(pick, not_pick)
        
        return dp[n-1]
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        num_1 = nums[0 : n-1]
        num_2 = nums[1: n]

        return max(self.house_robber_1(num_1), self.house_robber_1(num_2))
        