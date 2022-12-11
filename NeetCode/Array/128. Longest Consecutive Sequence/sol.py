# TC and Sc: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_consecutive_elements_sequence = 0
        
        for i in range(len(nums)):
            cur_num = nums[i]
            
            # check if this is the first occurance
            if cur_num - 1 in set_nums:
                continue
            
            count = 1
            while cur_num + 1 in set_nums:
                count += 1
                cur_num += 1
            
            longest_consecutive_elements_sequence = max(longest_consecutive_elements_sequence, count)
                
        return longest_consecutive_elements_sequence
            