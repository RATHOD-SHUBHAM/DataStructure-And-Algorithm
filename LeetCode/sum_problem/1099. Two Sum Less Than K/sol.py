class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n < 2:
            return -1

        nums.sort()

        left = 0
        right = n - 1

        max_sum = -1

        while left < right:
            cur_sum = nums[left] + nums[right]

            if cur_sum >= k:
                '''Reduce the sum'''
                right -= 1
            elif cur_sum < k:
                '''Capture and Increase the sum'''
                left += 1
                max_sum = max(max_sum, cur_sum)
        
        return max_sum

            