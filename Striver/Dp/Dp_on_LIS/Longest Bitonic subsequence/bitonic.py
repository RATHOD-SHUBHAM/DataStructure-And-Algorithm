from typing import List


class Solution:
    def LIS(self, nums):
        n = len(nums)
        
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    cur = 1 + dp[j]
                    dp[i] = max(dp[i], cur)
            
        return dp
        
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        # code here
        lis = self.LIS(nums)
        reverse_lis = self.LIS(nums[::-1])
        lds = reverse_lis[::-1]
        
        longest_bitonic_sub = 0
        for i in range(n):
            # For a valid bitonic sequence at position i:
            # - There must be at least one element before i that's smaller (lis[i] > 1)
            # - There must be at least one element after i that's smaller (lds[i] > 1)
            if lis[i] == 1 or lds[i] == 1:
                continue
            cur_len = (lis[i] + lds[i]) - 1
            longest_bitonic_sub = max(longest_bitonic_sub, cur_len)
        
        return longest_bitonic_sub
            
        
        
        
