class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            

            elif nums[mid] > nums[right]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            elif nums[mid] < nums[right]:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                # nums[mid] == nums[right]: can't tell which half is sorted, so reduce the right
                right = right - 1
            
        return False



# ========================== Trim Duplicates ==========================

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:

            # Skip Duplicates
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            
            while left < right and nums[right] == nums[right - 1]:
                right -= 1


            # Search in distinct sorted array
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True
            

            elif nums[mid] > nums[right]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # elif nums[mid] < nums[right]:
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            
        return False