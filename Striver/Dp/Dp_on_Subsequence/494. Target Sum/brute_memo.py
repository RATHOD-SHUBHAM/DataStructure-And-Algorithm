class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        idx = n - 1

        cur_sum = 0

        memo = {}

        return self.recursion(idx, cur_sum, memo, nums, target)
    
    def recursion(self, idx, cur_sum, memo, nums, target):
        if idx < 0:
            if cur_sum == target:
                return 1
            else:
                return 0
            
        if (idx, cur_sum) in memo:
            return memo[(idx, cur_sum)]
        
        # Take +
        take_pos = self.recursion(idx - 1, cur_sum + nums[idx], memo, nums, target)

        # Take - 
        take_neg = self.recursion(idx - 1, cur_sum - nums[idx], memo, nums, target)

        memo[(idx, cur_sum)] = take_pos + take_neg

        return memo[(idx, cur_sum)]