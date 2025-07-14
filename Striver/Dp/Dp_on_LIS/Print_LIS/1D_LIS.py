class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1 for _ in range(n+1)] # Every element is a subsequence of itself

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    take = 1 + dp[j] # add the cur number to previous LIS
                    dp[i] = max(dp[i], take)
        
        return max(dp)