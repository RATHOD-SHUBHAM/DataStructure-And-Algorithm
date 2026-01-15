# Formula: Product of all element on left * Product of all element on right

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_arr = [1] * n
        nxtProd = nums[0]
        for i in range(1, n):
            left_arr[i] = nxtProd
            nxtProd = left_arr[i] * nums[i]
        

        right_arr = [1] * n
        nxtProd = nums[-1]
        for i in reversed(range(n-1)):
            right_arr[i] = nxtProd
            nxtProd = right_arr[i] * nums[i]


        prod = [1] * n
        for i in range(n):
            prod[i] = left_arr[i] * right_arr[i]
        
        return prod

