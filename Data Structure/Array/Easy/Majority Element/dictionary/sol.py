'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?


'''



# Time Complexity = O(n**2)
# Space Complexity = O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicti = {}
        majority = len(nums) // 2
        
        for i in range(len(nums)):
            if nums[i] in dicti:
                dicti[nums[i]] += 1
            else:
                dicti[nums[i]] = 1
            
            
        for i in dicti:
            if dicti[i] > majority:
                return i