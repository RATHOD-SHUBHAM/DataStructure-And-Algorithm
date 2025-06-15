class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        idx = 0

        memo = {}

        return self.recursion(idx, memo, n, nums)
    
    def recursion(self, idx, memo, n, nums):
        # base case
        if idx == n-1:
            return True
        
        if idx >= n:
            return False
        
        if nums[idx] == 0:
            # we cannot move further
            return False

        if idx in memo:
            return memo[idx]
        
        # Logic
        canJump = False
        for jump in range(1, nums[idx] + 1):
            curJump = self.recursion(idx + jump, memo, n, nums)
            canJump = canJump or curJump
        
        memo[idx] = canJump

        return memo[idx]
