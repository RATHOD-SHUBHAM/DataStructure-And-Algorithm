# ------------------------ Set -------------------------

# Tc: and Sc O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        set_s = set(nums)

        for i in range(n):
            if i not in set_s:
                return i
        
        return n
    


# ------------------------ Gauss Algorithm -------------------------

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
    

# ------------------------ Bit Manipulation -------------------------

# Tc: O(n) | Sc: O(1)

# Gauss Formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        xor_n = 0
        for i in range(n+1):
            xor_n = xor_n ^ i
        


        xor_nums = 0
        for i in nums:
            xor_nums = xor_nums ^ i


        return xor_n ^ xor_nums