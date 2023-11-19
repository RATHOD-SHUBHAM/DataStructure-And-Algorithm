# Tc: O(n^3) | Sc: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        
        for i in range(len(nums)):
            cur_streak = 1
            cur_num = nums[i]
            
            while cur_num + 1 in nums:
                cur_num = nums[i] + 1
                cur_streak += 1
            
            longest_streak = max(longest_streak, cur_streak)
            
        return longest_streak