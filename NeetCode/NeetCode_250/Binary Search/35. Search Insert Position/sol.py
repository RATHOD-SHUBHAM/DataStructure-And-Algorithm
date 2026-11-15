class Solution:
    def bisect_left(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            
        return left
    
    def bisect_right(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
            
        return left

    def searchInsert(self, nums: list[int], target: int) -> int:
        idx_left = self.bisect_left(nums, target)
        print(idx_left)

        idx_right = self.bisect_right(nums, target)
        print(idx_right)

        return idx_left # or idx_right