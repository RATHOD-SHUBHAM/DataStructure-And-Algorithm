class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        idx = n - 1

        cur_sum = 0

        return self.recursion(idx, cur_sum, nums, target)
    
    def recursion(self, idx, cur_sum, nums, target):
        if idx < 0:
            if cur_sum == target:
                return 1
            else:
                return 0
        
        # Take +
        take_pos = self.recursion(idx - 1, cur_sum + nums[idx], nums, target)

        # Take - 
        take_neg = self.recursion(idx - 1, cur_sum - nums[idx], nums, target)

        return take_pos + take_neg