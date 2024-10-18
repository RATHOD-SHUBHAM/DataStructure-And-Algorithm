# Tc: O(log(n)) | Sc: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            
            mid = left + (right - left) // 2

            if nums[left] < nums[mid]:
                # Smallest number cannot be in between this range
                left = mid + 1
            else:
                if mid - 1 != -1 and nums[mid] < nums[mid - 1]:
                    # Eg: [5, 0, 1]
                    return nums[mid]
                elif mid + 1 != n and nums[mid] > nums[mid + 1]:
                    # Eg : [1, 0]
                    return nums[mid + 1]
                else:
                    right = mid - 1
                