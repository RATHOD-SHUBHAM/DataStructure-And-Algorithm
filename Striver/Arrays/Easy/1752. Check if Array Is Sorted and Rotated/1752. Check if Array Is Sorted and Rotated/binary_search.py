'''
    We Know that when an array is sorted 
        right > left

    When the array is rotated
        - if mid > right:
            then left of mid is all smaller than mid and greater than left
        
        - if mid < right:
            then right side of mid is all greater than mid and less than right
'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # if the array is just sorted and not rotated
        if nums == sorted(nums):
            return True

        left = 0
        right = n - 1

        # Handle Duplicate Values
        while left < right and nums[left] == nums[right]:
            left += 1

        while left < right:
            # Inflation point
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # left side is in increasing order - so check left for rotation point
                left = mid + 1
            else:
                # right side is in increasing order - so check left for rotation point
                right = mid
        
        rotation_point = left # or right

        if nums[rotation_point :] + nums[ : rotation_point] == sorted(nums):
            return True
        else:
            return False
        
