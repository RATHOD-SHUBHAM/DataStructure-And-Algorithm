# Brute Force ------------------------------------------------

# Tc :O(n^2) | Sc :O(n)

'''
    rotate the array every time and check if it is sorted
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            if nums == sorted(nums):
                return True
            
            # rotate array once
            nums = nums[1 : ] + [nums[0]]

        return False
    
# Better Brute ------------------------------------------------

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        i = 1

        inflation_point = 0

        while i < n:
            if nums[i-1] <= nums[i]:
                i += 1
            else:
                inflation_point = i
                break
        
        if nums[inflation_point :] + nums[ : inflation_point] == sorted(nums):
            return True
        else:
            return False
    

# Binary Search ------------------------------------------------


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

        # Handle Duplicate Values : Only for last elements [eg: 1 1 2 1]. 
        while left < right and nums[left] == nums[right]:
            left += 1

        # Findig the lowest point
        while left < right:
            # Inflation point
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # left side is in increasing order - so check left for rotation point
                left = mid + 1
            else:
                # right side is in increasing order - so check left for rotation point
                right = mid # this should be mid becuase, there can be a chance that this mid could be the potential inflation point [eg: 7 9 1 1 3]
        
        rotation_point = left # or right

        if nums[rotation_point :] + nums[ : rotation_point] == sorted(nums):
            return True
        else:
            return False
        
