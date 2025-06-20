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
    
# ----------------- Memoization -----------------

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

# ----------------- Tabulation -----------------
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [math.inf for _ in range(n)]
        dp[n-1] = 0

        for idx in reversed(range(n-1)):
            if nums[idx] == 0:
                continue
            # Logic
            for i in range(1, nums[idx] + 1):
                if idx + i >= n:
                    continue
                nxt_jump = 1 + dp[idx+i]
                dp[idx] = min(dp[idx], nxt_jump)
            
        # print(dp)
        return dp[0]

# ----------------- Greedy -----------------
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        jump_boundary = 0
        farthest = 0

        jump = 0

        for i in range(n-1):
            cur_jump = i + nums[i]
            farthest = max(farthest , cur_jump)

            if i == jump_boundary:
                jump += 1
                jump_boundary = farthest
        
        return jump