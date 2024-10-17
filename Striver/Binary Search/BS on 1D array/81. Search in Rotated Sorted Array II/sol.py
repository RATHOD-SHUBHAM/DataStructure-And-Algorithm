"""
To avoid duplicates, we can refer to the solution to Problem 15: 3 Sum, which is

while left < right and nums[left] == nums[left - 1]:
    left += 1

while left < right and nums[right] == nums[right + 1]:
    right -= 1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            
            mid = left + (right - left) // 2


            if nums[mid] == target:
                return True
            
            if nums[left] <= nums[mid]:
                # we know for sure left to mid are in order
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # nums[mid] < nums[right]
                # we know that mid to right are in order
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return False