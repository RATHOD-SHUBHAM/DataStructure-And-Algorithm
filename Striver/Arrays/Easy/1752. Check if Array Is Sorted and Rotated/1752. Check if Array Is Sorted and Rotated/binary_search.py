# Binary Search

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
        sorted_nums = sorted(nums)

        left = 0
        right = n - 1

        inflation_point = self.binarySearch(left, right, nums)

        new_nums = nums[inflation_point : ] + nums[ : inflation_point]

        return new_nums == sorted_nums

    def binarySearch(self, left, right, nums):

        # Handle Duplicate Values
        while left < right and nums[left] == nums[right]:
            left += 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # The inflation point is on the right
                left = mid + 1
            elif nums[mid] <= nums[right]:
                # Mid can be the inflation point or the inflation point is on the left
                right = mid
        
        return left
