class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        op = [None] * n

        cur_sum = 0

        for i in range(n):
            cur_sum += nums[i]
            op[i] = cur_sum
        return op