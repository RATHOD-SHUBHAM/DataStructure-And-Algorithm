# Tc: O(n) | Sc: O(1)

# Kadene's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_subarray_sum = cur_sum = nums[0]

        for i in range(1, n):
            cur_sum = max(nums[i] , cur_sum + nums[i])
            max_subarray_sum = max(max_subarray_sum , cur_sum)
        
        return max_subarray_sum