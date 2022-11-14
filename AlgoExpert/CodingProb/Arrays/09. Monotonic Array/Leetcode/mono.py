"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105

"""

# Time and Space: O(n) | O(1)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # initially I dont know weather the number is increasing or decreasing
        increasing = False
        decreasing = False
        
        # if both flip: Meaning it is both increasing and decresing
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increasing = True
            elif nums[i] < nums[i-1]:
                decreasing = True
        
        # both flipped: Meaning numbers increased and decreased
        if increasing== True and decreasing == True: 
            return False
        else:
            return True