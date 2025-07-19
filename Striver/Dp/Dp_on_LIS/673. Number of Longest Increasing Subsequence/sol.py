class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n
        count = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        count[i] = count[j]
                    
                    # this is another subseq with which the cur_ele can attach itself
                    elif dp[i] == 1 + dp[j]:
                        count[i] += count[j]
        
        max_count = max(count)
        no_of_lis = 0

        for i in range(n):
            if count[i] == max_count:
                no_of_lis += count[i]
        
        return no_of_lis
