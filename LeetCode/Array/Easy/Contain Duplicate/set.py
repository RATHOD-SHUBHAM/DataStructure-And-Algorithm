'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


'''

'''
True - if any element appears twice
False - if all the elements are unique

'''

# Time Complexity: O(n)
#  Iterating over a list is O(n) and adding each element to the hash set is O(1), so the total operation is O(n).

# space complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # method1
        # if len(set(nums)) != len(nums):
        #     return True
        # else:
        #     return False
        
        # method2
        # res = True if len(set(nums)) != len(nums) else False
        
        # return res
        

        # method3
        return (True if len(set(nums)) != len(nums) else False)
