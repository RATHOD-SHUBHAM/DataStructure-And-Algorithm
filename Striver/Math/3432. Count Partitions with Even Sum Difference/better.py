# Tc: O(n)
# Sc: O(1)

"""
arr_1 + arr_2 = total_sum -> eq1

We want |arr_1 - arr_2| to be even

so from eq1 we can say:
arr_2 = total_sum - arr_1

"""

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        total = sum(nums)
        arr_1 = 0

        for i in range(1, n):
            arr_1 += nums[i]
            arr_2 = total - arr_1

            diff = abs(arr_1 - arr_2)

            if diff % 2 == 0:
                count += 1
        
        return count