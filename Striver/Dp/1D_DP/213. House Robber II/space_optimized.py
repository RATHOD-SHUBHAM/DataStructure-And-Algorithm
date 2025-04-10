class Solution:
    def optimized(self, nums):
        n = len(nums)
        
        p_prev = 0
        cur_pick = prev = nums[0]

        for i in range(1, n):
            pick = nums[i] + (p_prev if i-2 >= 0 else 0) # the brackets are important
            not_pick = 0 + (prev if i-1 >= 0 else 0)

            cur_pick = max(pick, not_pick)

            p_prev = prev
            prev = cur_pick
        
        return cur_pick
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return nums[0]

        num_1 = nums[0 : n-1]
        num_2 = nums[1: n]

        return max(self.optimized(num_1), self.optimized(num_2))
        