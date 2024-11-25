class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if i == 0 and nums[i+1] < nums[i]:
                return i

            if i == n-1 and nums[i-1] < nums[i]:
                return i

            elif nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i