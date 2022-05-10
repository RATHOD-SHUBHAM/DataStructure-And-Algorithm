# Time = O(n)
# space = O(1) if op is not counted
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_ = [1] * len(nums)
        
        # keep calculating the left value except self
        cur_left_product = 1
        for i in range(len(nums)):
            product_[i] = cur_left_product
            cur_left_product *= nums[i]
            
        # calculate the right value except self
        cur_right_product = 1
        for i in reversed(range(len(nums))):
            product_[i] *= cur_right_product
            cur_right_product *= nums[i]
            
        return product_