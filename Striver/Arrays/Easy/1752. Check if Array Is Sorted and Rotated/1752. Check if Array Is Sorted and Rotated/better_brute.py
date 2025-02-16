# Inflation point

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_nums = sorted(nums)

        inflation_point = 0

        for i in range(1, n):
            # Compare to previous element to get the inflation point
            if nums[i-1] > nums[i]:
                inflation_point = i
        
        new_nums = nums[inflation_point : ] + nums[ : inflation_point]

        return new_nums == sorted_nums