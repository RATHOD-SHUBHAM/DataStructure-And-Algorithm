class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0

        prev_idx = -1

        return self.recursion(idx, prev_idx, n, nums)
    
    def recursion(self, idx, prev_idx, n, nums):
        # base case
        if idx == n:
            return 0
        
        # Logic
        if prev_idx == -1 or nums[idx] > nums[prev_idx]:
            take = 1 + self.recursion(idx + 1, idx, n, nums)
        else:
            take = 0
        
        no_take = 0 + self.recursion(idx + 1, prev_idx, n, nums)

        return max(take, no_take)