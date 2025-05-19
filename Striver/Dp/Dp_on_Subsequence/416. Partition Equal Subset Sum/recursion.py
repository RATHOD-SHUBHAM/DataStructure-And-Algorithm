class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        idx = n - 1

        cur_sum = 0

        return self.recursion(idx, nums, n, cur_sum, total_sum)
    
    def recursion(self, idx, nums, n, cur_sum, total_sum):
        # base case
        if cur_sum == total_sum // 2:
            return True

        if idx < 0:
            return False
        

        take = self.recursion(idx-1, nums, n, cur_sum + nums[idx], total_sum)
        dont_take = self.recursion(idx-1, nums, n, cur_sum, total_sum)

        return take or dont_take