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

# Time: O(n)
# Space: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        counter = collections.Counter(nums)
        
        # print(majority)
        # print(counter)
        
        for i in counter:
            if counter[i] > majority:
                return i
                # print(i) 
        
        

# brute force
'''
n = size of array
majority = element that appears more than ⌊n / 2⌋ times.
majority always exists.


majority = len(nums) //  2 = 1
nums = [3,2,3]

c = collections.Counter(nums)

{
 3:2
 2:1
 }
 
 for i in c:
     if c[i] > majority:
        return i
        
        
        
--------------------
majority = len(nums) //  2 = 7//2 = 3
nums = [2,2,1,1,1,2,2]

c = collections.Counter(nums)

{
 2:4
 1:3
 }
 
 for i in c:
     if c[i] > majority:
        return i


'''