'''
The question currently says : whose sum is greater than or equal to target
But what if the question was : whose sum is equal to target
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        left = 0

        min_subarray_len = math.inf

        cur_sum = 0

        for right in range(n):
            cur_sum += nums[right]

            if cur_sum == target:
                window_len = (right - left) + 1
                min_subarray_len = min(min_subarray_len, window_len)
            
            while cur_sum > target:
                cur_sum -= nums[left]
                left += 1

                if cur_sum == target:
                    window_len = (right - left) + 1
                    min_subarray_len = min(min_subarray_len, window_len)
            
        return min_subarray_len if min_subarray_len != math.inf else 0
