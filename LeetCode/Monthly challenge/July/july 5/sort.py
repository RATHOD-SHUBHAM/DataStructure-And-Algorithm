# TC: O(nlogn)
#SC: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        longest_seq = 1
        cur_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    cur_streak += 1
                else:
                    longest_seq = max(longest_seq , cur_streak)
                    cur_streak = 1
                    
        return max(longest_seq , cur_streak)