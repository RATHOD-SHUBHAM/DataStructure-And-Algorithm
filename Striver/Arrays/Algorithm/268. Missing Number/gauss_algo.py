# Tc: O(n) | Sc: O(1)

# Gauss Formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # Sum of n natural number = ( n * (n+1) ) // 2
        sum_n_natural_number = ( n * (n + 1) ) // 2
        current_n_sum = sum(nums)

        missing_number = sum_n_natural_number - current_n_sum

        return missing_number
        