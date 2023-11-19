# Tc: O(n) | Sc: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)
        longest_streak = 0
        
        for i in range(len(nums)):
            cur_num = nums[i]
            # check if this is the starting number
            if cur_num - 1 not in hash_nums:
                cur_streak = 1
            
                while cur_num + 1 in hash_nums:
                    cur_num += 1
                    cur_streak += 1

                longest_streak = max(longest_streak, cur_streak)
            
        return longest_streak