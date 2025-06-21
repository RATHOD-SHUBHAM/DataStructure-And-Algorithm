class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0
        memo = {}

        return self.recursion(idx, memo, n, nums)
    
    def recursion(self, idx, memo, n, nums):
        # base case
        if idx == n - 1:
            return 0
        
        if idx > n-1 or nums[idx] == 0:
            return math.inf
        
        if idx in memo:
            return memo[idx]
        
        # Logic
        min_jump = math.inf
        for i in range(1, nums[idx] + 1):
            cur_jump = 1 + self.recursion(idx + i, memo, n, nums)
            min_jump = min(min_jump , cur_jump)
        
        memo[idx] = min_jump

        return memo[idx]


