# similar to : 740. Delete and Earn
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        p_prev_amount = nums[0]
        prev_amount = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            cur_sum = nums[i]
            
            cur_amount = max(cur_sum + p_prev_amount, prev_amount)
            
            p_prev_amount = prev_amount
            prev_amount = cur_amount
            
        return prev_amount
            