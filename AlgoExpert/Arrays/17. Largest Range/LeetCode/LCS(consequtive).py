'''

128. Longest Consecutive Sequence
Medium


Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


'''

# Time and Space = O(n) | O(n)
# Check notes
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_range = 0
        nums_set = set(nums)
        
        for num in nums_set:
            # Check if it is the beginning of the range
            if num - 1 not in nums_set:
                cur_num = num
                cur_range_len = 1
                
                # look for next consecutive number
                while cur_num + 1 in nums_set:
                    cur_num = cur_num + 1
                    cur_range_len += 1
                    
                longest_range = max(longest_range , cur_range_len)
                
        return longest_range
                    
                