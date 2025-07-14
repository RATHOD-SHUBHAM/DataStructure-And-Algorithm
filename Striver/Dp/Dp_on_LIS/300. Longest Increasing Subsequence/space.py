class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0 for _ in range(n+1)]

        for idx in reversed(range(n)):
            cur = [0 for _ in range(n+1)]
            for prev_idx in reversed(range(-1, idx)):
                # Logic
                if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                    take = 1 + dp[idx+1]
                else:
                    take = 0
                
                no_take = 0 + dp[prev_idx + 1]

                cur[prev_idx + 1] = max(take, no_take)
            
            dp = cur
                
        return dp[0]