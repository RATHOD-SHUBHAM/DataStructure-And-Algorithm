# Tc: O(n^2)
# Sc: O(1)

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n): # O(n)
            arr_1 = sum(nums[ : i]) # O(n)
            arr_2 = sum(nums[i : ])

            diff = abs(arr_1 - arr_2)

            if diff % 2 == 0:
                count += 1
        
        return count
    
# ---------------------- Better Approach ----------------------
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
    
# ---------------------- Optimal Approach ----------------------
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)

        """
        We know
        total = arr_1 + arr_2 
        arr_2 = total - arr_1 -> eq1

        We know
        diff = arr_1 - arr_2 -> eq2

        eq2 in eq1
        diff = arr_1 - (total - arr_1)
        diff = 2 * arr_1 - total

        anything multiplied by 2 is even
        """

        if total % 2 == 0:
            return n - 1
        
        return 0