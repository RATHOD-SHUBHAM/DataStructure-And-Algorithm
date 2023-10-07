# Tc: O(n^3) | Sc: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_subarray_sum = -math.inf
        
        for i in range(n):
            for j in range(i, n):
                cur_sum = 0

                for k in range(i, j+1):
                    cur_sum += nums[k]
                    max_subarray_sum = max(max_subarray_sum , cur_sum)
        
        return max_subarray_sum