"""
The key is to keep two different notions of “prev_idx” straight:

prev_idx (the variable) in your loops is always the actual array index of the last-chosen element (ranging from -1 to n–1).

prev_idx + 1 is only used when you index into the DP table, because column 0 of the table represents prev_idx = –1.

So we need to adjust prev_idx pointer by adding 1 when we use it to index into the DP table.

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0 for _ in range(n+1)]for _ in range(n+1)]

        for idx in reversed(range(n)):
            for prev_idx in reversed(range(-1, idx)):
                # Logic
                if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                    """
                    In the DP table, columns are labeled by prev_idx + 1.
                    So if your new prev_idx is idx, the column you jump to is (idx) + 1
                    """
                    take = 1 + dp[idx+1][idx+1] 
                else:
                    take = 0
                
                no_take = 0 + dp[idx+1][prev_idx+1]

                dp[idx][prev_idx+1] = max(take, no_take)

        return dp[0][0]