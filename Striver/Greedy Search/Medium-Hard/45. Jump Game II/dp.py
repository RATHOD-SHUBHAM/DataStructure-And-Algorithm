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