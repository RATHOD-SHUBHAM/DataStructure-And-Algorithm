class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()

        MOD = (10 ** 9) + 7

        left = 0 # consider this to be my minimum number
        right = n - 1

        count = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                no_of_subsequence = 2 ** (right - left)
                count += no_of_subsequence % MOD
                left += 1
            else:
                right -= 1
        
        return count % MOD
    
# --------------------- Avoide Overflow ---------------------
"""
You're taking no_of_subsequence % MOD but then adding it to count without taking modulo again. This means count itself can grow very large and exceed the modulo value.

Computing 2 ** (right - left) can be very expensive and cause overflow

Use pow(2, right - left, MOD) instead of 2 ** (right - left) - this efficiently computes (2^(right-left)) % MOD without overflow
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()

        MOD = (10 ** 9) + 7

        left = 0 # consider this to be my minimum number
        right = n - 1

        count = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                no_of_subsequence = pow(2, (right-left), MOD)
                count += no_of_subsequence
                left += 1
            else:
                right -= 1
        
        return count % MOD