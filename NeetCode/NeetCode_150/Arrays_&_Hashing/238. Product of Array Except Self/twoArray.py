# Using 2 array for - running prod
# Tc & Sc: O(n) | O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Left Running Sum
        left_prod = [1] * n
        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i-1]
        
        # Right Running Sum
        right_prod = [1] * n
        for i in reversed(range(n-1)):
            right_prod[i] = right_prod[i+1] * nums[i+1]

        op = [1] * n
        for i in range(n):
            op[i] = left_prod[i] * right_prod[i]
        

        return op
