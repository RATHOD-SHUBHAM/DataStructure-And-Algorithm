#-------------------------- Mid Right ---------------------------------------

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left < right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[right]:
                # Here I am sure that left value will always be smaller than or equal to mid
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1 
            else:
                # Here I am sure that right value will always be greater than or equal to mid
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        

        if nums[right] == target:
            return right
        else:
            return -1
                
#-------------------------- Mid Left ---------------------------------------

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[left]:
                # Right side is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
            else:
                # left side is sorted
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1