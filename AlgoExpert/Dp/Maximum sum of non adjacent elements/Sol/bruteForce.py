# Tc: O(n^2) | Sc: O(n^2)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recursion(n - 1, nums)
        
        
    def recursion(self, idx, nums):
        # base case
        if idx < 0:
            return 0
        
        if idx == 0:
            return nums[0]
        
        pick = nums[idx] + self.recursion(idx - 2, nums)
        dontPick = 0 + self.recursion(idx - 1, nums)
        
        return max(pick, dontPick)



# https://leetcode.com/discuss/interview-question/702177/apple-phone-maximum-sum-of-non-adjacent-elements
# https://leetcode.com/problems/house-robber/