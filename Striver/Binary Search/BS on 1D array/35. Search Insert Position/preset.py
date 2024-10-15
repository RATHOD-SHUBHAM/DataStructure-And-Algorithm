# With preset value

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        ans = n

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            
            else: # nums[mid] >= target
                ans = mid
                right = mid - 1

        return ans