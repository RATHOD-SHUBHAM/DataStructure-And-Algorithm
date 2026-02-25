# Using 1 array for - running prod
# Tc & Sc: O(n) | O(1) # The problem statement mentions that using the answer array doesn't add to the space complexity.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Left Running Sum
        prod = [1] * n
        for i in range(1, n):
            prod[i] = prod[i - 1] * nums[i-1]
        
        # Right Running Sum
        right_prod = 1
        for i in reversed(range(n-1)):
            right_prod = right_prod * nums[i+1]
            prod[i] = prod[i] * right_prod
        

        return prod
