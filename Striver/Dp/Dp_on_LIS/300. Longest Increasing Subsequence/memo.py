class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0

        prev_idx = -1

        memo= {}

        return self.recursion(idx, prev_idx, memo, n, nums)
    
    def recursion(self, idx, prev_idx, memo, n, nums):
        # base case
        if idx == n:
            return 0
        
        if (idx, prev_idx) in memo:
            return memo[(idx, prev_idx)]
        
        # Logic
        if prev_idx == -1 or nums[idx] > nums[prev_idx]:
            take = 1 + self.recursion(idx + 1, idx, memo, n, nums)
        else:
            take = 0
        
        no_take = 0 + self.recursion(idx + 1, prev_idx, memo, n, nums)

        memo[(idx, prev_idx)] = max(take, no_take)
        
        return memo[(idx, prev_idx)]