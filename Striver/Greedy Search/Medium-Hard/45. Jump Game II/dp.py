class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [math.inf for _ in range(n)]
        # base case
        dp[n-1] = 0

        # logic
        for idx in reversed(range(n-1)):
            if nums[idx] == 0:
                continue

            # Logic
            for i in range(1, nums[idx] + 1):
                if idx + i > n-1:
                    continue
                
                cur_jump = 1 + dp[idx + i]
                dp[idx] = min(dp[idx] , cur_jump)
        
        return dp[0]