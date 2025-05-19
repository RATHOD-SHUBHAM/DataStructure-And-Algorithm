class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        idx = n - 1

        cur_sum = 0

        memo = {}

        return self.recursion(idx, nums, memo, n, cur_sum, total_sum)
    
    def recursion(self, idx, nums, memo, n, cur_sum, total_sum):
        # base case
        if cur_sum == total_sum // 2:
            return True

        if idx < 0:
            return False
        
        if (idx, cur_sum) in memo:
            return memo[(idx, cur_sum)]
        

        take = self.recursion(idx-1, nums, memo, n, cur_sum + nums[idx], total_sum)
        dont_take = self.recursion(idx-1, nums, memo, n, cur_sum, total_sum)

        memo[(idx, cur_sum)] = take or dont_take

        return memo[(idx, cur_sum)]