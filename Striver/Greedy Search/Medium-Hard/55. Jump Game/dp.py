class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [False for _ in range(n)]

        # base case
        dp[n-1] = True

        for i in reversed(range(n-1)):
            # Base
            if nums[i] == 0:
                dp[i] = False
                continue
            
            # Logic
            canJump = False
            for jump in range(1, nums[i] + 1):
                if i + jump < n:
                    curJump = dp[i + jump]
                    canJump = canJump or curJump
            
            dp[i] = canJump
        
        return dp[0]
    