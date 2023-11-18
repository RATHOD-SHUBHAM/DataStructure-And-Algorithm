# Running Product - Tc: O(1) and Sc: O(1) 
# Question states: (The output array does not count as extra space for space complexity analysis.)
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
        running_prod = nums[n-1]
        for i in reversed(range(n-1)):
            left_product[i] *= running_prod

            running_prod *= nums[i]
        
        # print(left_product)

        return left_product