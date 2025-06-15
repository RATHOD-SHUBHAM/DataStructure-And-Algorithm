class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        idx = 0

        return self.recursion(idx, n, nums)
    
    def recursion(self, idx, n, nums):
        # base case
        if idx == n-1:
            return True
        
        if idx >= n:
            return False
        
        if nums[idx] == 0:
            # we cannot move further
            return False
        
        # Logic
        canJump = False
        for jump in range(1, nums[idx] + 1):
            curJump = self.recursion(idx + jump, n, nums)
            canJump = canJump or curJump
        
        return canJump
