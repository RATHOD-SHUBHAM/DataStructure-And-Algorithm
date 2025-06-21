class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0

        return self.recursion(idx n, nums)
    
    def recursion(self, idx, n, nums):
        # base case
        if idx == n - 1:
            return 0
        
        if idx > n-1 or nums[idx] == 0:
            return math.inf
        
        # Logic
        min_jump = math.inf
        for i in range(1, nums[idx] + 1):
            cur_jump = 1 + self.recursion(idx + i, n, nums)
            min_jump = min(min_jump , cur_jump)
        
        return min_jump





# ----------------------- Same Solution ------------------------
class Solution:
    def __init__(self):
        self.min_jump = math.inf

    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0
        count = 0

        self.recursion(idx, count, nums, n)

        return self.min_jump
    
    def recursion(self, idx, count, nums, n):
        # base case
        if idx == n - 1:
            self.min_jump = min(self.min_jump , count)
        
        if idx > n - 1:
            return
        
        # Logic
        for i in range(1, nums[idx] + 1):
            self.recursion(idx + i, count + 1, nums, n)
        
        return
        