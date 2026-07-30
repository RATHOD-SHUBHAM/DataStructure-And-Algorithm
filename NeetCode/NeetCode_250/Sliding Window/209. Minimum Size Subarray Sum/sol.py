# Tc: O(n) | Sc: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        left = 0

        min_subarray_len = math.inf

        cur_sum = 0

        for right in range(n):
            cur_sum += nums[right] # Extend the current window

        # When sum is greater than or equal to target, get the current window length and keep shrinking the window
            while cur_sum >= target:
                window_len = (right - left) + 1
                min_subarray_len = min(min_subarray_len, window_len)

                cur_sum -= nums[left]
                left += 1
            
            
        return min_subarray_len if min_subarray_len != math.inf else 0

