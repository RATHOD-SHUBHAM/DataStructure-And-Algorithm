class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0

        return self.recursion(idx, n, nums)
    
    def recursion(self, idx, n, nums):
        # Base case
        if idx == n-1:
            return 0
        
        if idx >= n:
            return math.inf
        
        if nums[idx] == 0:
            return math.inf
        
        
        # Logic
        min_jump = math.inf
        for jump in range(1, nums[idx] + 1):
            can_jump = self.recursion(idx + jump, n, nums)
            min_jump = min(can_jump , min_jump)
        
        return 1 + min_jump