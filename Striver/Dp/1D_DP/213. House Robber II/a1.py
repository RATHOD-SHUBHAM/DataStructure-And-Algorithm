# -------------- recursion ----------------------
class Solution:
    def recursion(self, n, nums):
        if n < 0:
            return 0
        
        if n == 0:
            return nums[0]
        
        pick = nums[n] + self.recursion(n-2, nums) # Cannot moce to adjacent house
        not_pick = 0 + self.recursion(n-1, nums) # If we dont pick current house, we can move to adjacent house

        return max(pick, not_pick)

    def house_robber_1(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recursion(n-1, nums)
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        num_1 = nums[0 : n-1]
        num_2 = nums[1: n]

        return max(self.house_robber_1(num_1), self.house_robber_1(num_2))

# ------------------------ Memoization ----------------------
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

# ------------------------ Tabulation ----------------------
# class Solution:
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

# ------------------------ Space Optimization ----------------------
class Solution:
    def optimized(self, nums):
        n = len(nums)
        
        p_prev = 0
        cur_pick = prev = nums[0]

        for i in range(1, n):
            pick = nums[i] + (p_prev if i-2 >= 0 else 0) # the brackets are important
            not_pick = 0 + (prev if i-1 >= 0 else 0)

            cur_pick = max(pick, not_pick)

            p_prev = prev
            prev = cur_pick
        
        return cur_pick
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        num_1 = nums[0 : n-1]
        num_2 = nums[1: n]

        return max(self.optimized(num_1), self.optimized(num_2))
        