# Follow up to Second largest problem
import math

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)

        largest = max(nums)
        # There are negative values
        second_largest = -math.inf
        third_largest = -math.inf

        for i in range(n):
            cur_ele = nums[i]

            if cur_ele == largest:
                continue

            if cur_ele > second_largest:
                third_largest = second_largest
                second_largest = cur_ele

            elif cur_ele < second_largest and cur_ele > third_largest:
                third_largest = cur_ele
        

        if third_largest == -math.inf:
            return largest
        else:
            return third_largest