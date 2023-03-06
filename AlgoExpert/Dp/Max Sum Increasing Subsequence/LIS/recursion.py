# Tc: O(2^n) | Sc: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        curIdx = 0
        prevIdx = -1 # we need to keep track of prev value as we need to increasing sub sequence
        
        return self.LIS(curIdx, prevIdx, nums)
    
    def LIS(self, curIdx, prevIdx, nums):
        # base case
        if curIdx >= len(nums):
            return 0
        
        max_len = 0
        
        # code
        dontTake = 0 + self.LIS( curIdx + 1, prevIdx , nums)
        max_len += dontTake
        
        if prevIdx == -1 or nums[curIdx] > nums[prevIdx]:
            take = 1 + self.LIS( curIdx + 1, curIdx, nums)
            max_len = max(max_len , take)
            
        return max_len