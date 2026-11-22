# The array is sorted, and has unique numbers
# so if we take the middle ele and check to the right, we will know that:
    # In actual sorted array , the mid has to be less than right.
    # if mid is greater than right, then we know array was rotated and smallest element are on right side 
    # if mid is smaller than right, we know that smallest element is possibly on left

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # search space is on the right
                left = mid + 1
            elif nums[mid] < nums[right]:
                # # search space is on the left
                right = mid
        
        return nums[left]