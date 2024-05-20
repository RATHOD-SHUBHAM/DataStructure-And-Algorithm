class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return nums

        nums.sort()

        left = 0
        right = n - 1

        mid = left + (right - left) // 2

        return nums[mid]