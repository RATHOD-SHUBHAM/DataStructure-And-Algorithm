class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [math.inf for _ in range(n)]

        # base case
        dp[n-1] = 0 # it take 0 steps to reach idx 0 from 0

        # Logic
        for idx in reversed(range(n-1)):
            min_jump = math.inf

            if nums[idx] == 0:
                continue
            
            for jump in range(1, nums[idx] + 1):
                can_jump = math.inf
                
                if idx + jump < n:
                    can_jump = dp[idx + jump]
                min_jump = min(can_jump , min_jump)
            
            dp[idx] = 1 + min_jump
                
        return dp[0]