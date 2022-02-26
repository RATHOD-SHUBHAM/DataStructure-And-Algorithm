'''
Two Sum



Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input may have duplicate solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15,10,-1], target = 9
Output: [[2,7], [10,-1]]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
No dupliactes are allowed.




'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        cache_set = set()
        
        for i in range(len(nums)):
            diff = target - nums[i]
            # prevent duplicate
            if len(res) == 0 or nums[i] != res[1][-1]:
                if diff in cache_set:
                    res.append([diff,nums[i]])
            cache_set.add(nums[i])
            
        return res