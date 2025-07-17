from typing import List


class Solution:
    def LIS(self, nums):
        n = len(nums)
        
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return dp
        
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        # code here
        lis = self.LIS(nums)
        reverse_lis = self.LIS(nums[::-1])
        reverse_lis = reverse_lis[::-1]
        
        max_bitonic_seq = 0
        for i in range(n):
            # For a valid bitonic sequence at position i:
            # - There must be at least one element before i that's smaller (lis[i] > 1)
            # - There must be at least one element after i that's smaller (reverse_lis[i] > 1)
            if lis[i] > 1 and reverse_lis[i] > 1:
                cur_seq = (lis[i] + reverse_lis[i]) - 1
                max_bitonic_seq = max(max_bitonic_seq, cur_seq)
        
        return max_bitonic_seq
