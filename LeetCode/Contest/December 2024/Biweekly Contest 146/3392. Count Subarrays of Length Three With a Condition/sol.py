class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        for i in range(n-2):
            subarray_sum = nums[i] + nums[i+2]

            if subarray_sum == nums[i+1] / 2:
                count += 1

        return count