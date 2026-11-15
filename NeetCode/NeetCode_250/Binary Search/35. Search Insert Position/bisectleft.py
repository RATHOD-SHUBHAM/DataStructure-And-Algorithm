class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx