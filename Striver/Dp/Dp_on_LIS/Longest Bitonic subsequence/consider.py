"""
Note: This will only work if
We cosnider a strictly increasing or a strictly decreasing sequence as a bitonic sequence
"""


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
            cur_seq = (lis[i] + reverse_lis[i]) - 1
            max_bitonic_seq = max(max_bitonic_seq, cur_seq)
        
        return max_bitonic_seq
