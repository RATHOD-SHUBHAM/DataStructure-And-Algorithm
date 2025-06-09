"""
Product of sum except self -> what this means is, 
    * Get me the product of all left side array.
    * Get me the product of all right side array.
    * Combine them together and that is the product of entire array except self.

For array 1, 2, 3, 4

Product of all array from left to 3, excluding 3 is 2
--------
1, 1, 2,| 4
--------

Product of all array from right to 3, excluding 3 is 4
        --------
24, 12, | 4, 1
        --------


Now combine left and right 2 * 4 = 8, this is product of array 3 except self

Visual
--------
1, 1, 2,| 4
--------
        --------
24,12,  |4, 1
        --------
==============
_ , _ , 8, _ 
==============
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Left running product
        left_prod = [1] * n

        running_prod = 1
        for i in range(n):
            left_prod[i] = running_prod
            # Now grab the prod
            running_prod *= nums[i]
        
        # Right running product
        right_prod = [1] * n

        running_prod = 1
        for i in reversed(range(n)):
            right_prod[i] = running_prod
            # Now grab the prod
            running_prod *= nums[i]
        
        # Now compute the product of sum except self
        prod = [1] * n
        for i in range(n):
            prod[i] = left_prod[i] * right_prod[i]
        
        return prod


# ------------------------- Optimized Solution -------------------------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Left running product
        prod = [1] * n

        running_prod = 1
        for i in range(n):
            prod[i] = running_prod
            # Now grab the prod
            running_prod *= nums[i]
        
        running_prod = 1
        for i in reversed(range(n)):
            prod[i] = running_prod * prod[i]
            # Now grab the prod
            running_prod *= nums[i]
        
        return prod
