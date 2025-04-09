class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.recursion(n-1, nums)
    
    def recursion(self, n, nums):
        if n < 0:
            return 0
        
        if n == 0:
            return nums[0]
        
        pick = nums[n] + self.recursion(n-2, nums) # Cannot moce to adjacent house
        not_pick = 0 + self.recursion(n-1, nums) # If we dont pick current house, we can move to adjacent house

        return max(pick, not_pick)