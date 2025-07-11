# ---------------------- Recursion ----------------------
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recursion(n-1, nums)
    
    def recursion(self, n, nums):
        if n < 0:
            return 0
        
        if n == 0:
            return nums[0]
        
        pick = nums[n] + self.recursion(n-2, nums) # Cannot moce to adjacent house
        not_pick = 0 + self.recursion(n-1, nums) # If we dont pick current house, we can move to adjacent house

        return max(pick, not_pick)
    

# ---------------------- Memoization ----------------------
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
    
# ---------------------- Tabulation ----------------------
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [-1] * n
        dp[0] = nums[0]

        for i in range(1, n):
            pick = nums[i] + (dp[i-2] if i-2 >= 0 else 0) # the brackets are important
            not_pick = 0 + (dp[i-1] if i-1 >= 0 else 0)

            dp[i] = max(pick, not_pick)
        
        return dp[n-1]
        
# ---------------------- Space Optimized ----------------------
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        p_prev = 0
        prev = 0
        
        for idx in range(n):
            # Logic
            pick = nums[idx] + p_prev
            no_pick = prev

            cur = max(pick, no_pick)

            p_prev = prev
            prev = cur
        
        return prev
    
        