'''

45. Jump Game II
Medium

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000


'''

# Time and Space = O(n) | O(1)

# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0 
        
        # left = one jump - min of one jump is possible
        left = 0
        #right = farthest jump
        right = 0
        
        # if my right reach the last element then i have reached destination
        while right < len(nums) - 1:
            farthest_jump = 0
            
            # calculate the max jump from all element
            for i in range(left, right+1):
                farthest_jump = max(farthest_jump , i + nums[i])
            
            jump_count += 1
            
            left = right+1
            right = farthest_jump
            
        return jump_count