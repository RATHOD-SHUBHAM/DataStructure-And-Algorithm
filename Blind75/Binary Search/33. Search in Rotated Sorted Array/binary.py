'''
    Divide the array into left and right and search
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            # find Inflation point
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[left]:
                # explore left section
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            elif nums[mid] < nums[right]:
                # explore right section
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

        