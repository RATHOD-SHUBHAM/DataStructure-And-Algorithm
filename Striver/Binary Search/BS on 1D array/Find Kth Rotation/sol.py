#User function Template for python3
class Solution:
    def findKRotation(self, nums):
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            if nums[left] <= nums[right]:
                return left % n
            
            mid = left + (right - left) // 2

            if nums[left] < nums[mid]:
                # Smallest number cannot be in between this range
                left = mid + 1
            else:
                if mid - 1 != -1 and nums[mid] < nums[mid - 1]:
                    # Eg: [5, 0, 1]
                    return mid % n
                elif mid + 1 != n and nums[mid] > nums[mid + 1]:
                    # Eg : [1, 0]
                    return mid + 1 % n
                else:
                    right = mid - 1