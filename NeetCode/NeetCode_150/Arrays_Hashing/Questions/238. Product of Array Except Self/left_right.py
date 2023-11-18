# Running Product - Tc and Sc: O(n) 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Left side running product
        left_product = [1] * n

        running_prod = nums[0]
        for i in range(1,n):
            left_product[i] = running_prod

            running_prod *= nums[i]
        
        # print(left_product)

        # right side running product
        right_product = [1] * n

        running_prod = nums[n-1]
        for i in reversed(range(n-1)):
            right_product[i] = running_prod

            running_prod *= nums[i]
        
        # print(right_product)

        # Product of array except self
        prod = [1] * n
        for i in range(n):
            prod[i] = left_product[i] * right_product[i]
        
        return prod