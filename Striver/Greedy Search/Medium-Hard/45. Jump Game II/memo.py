class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0

        memo = {}

        return self.recursion(idx, memo, n, nums)
    
    def recursion(self, idx, memo, n, nums):
        # Base case
        if idx == n-1:
            return 0
        
        if idx >= n:
            return math.inf
        
        if nums[idx] == 0:
            return math.inf
        
        if idx in memo:
            return memo[idx]
        
        
        # Logic
        min_jump = math.inf
        for jump in range(1, nums[idx] + 1):
            can_jump = self.recursion(idx + jump, memo, n, nums)
            min_jump = min(can_jump , min_jump)
        
        memo[idx] =  1 + min_jump

        return memo[idx]