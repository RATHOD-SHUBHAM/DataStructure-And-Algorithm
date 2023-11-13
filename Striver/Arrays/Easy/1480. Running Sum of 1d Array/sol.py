class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        running_sum = [0] * n
        running_sum[0] = nums[0]

        for i in range(1, n):
            running_sum[i] = nums[i] + running_sum[i-1]
        
        return running_sum