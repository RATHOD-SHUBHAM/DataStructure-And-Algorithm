class Solution:
    def rob(self, nums: List[int]) -> int:
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

# -------------------------- Same Solution ------------------
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 2:
            return nums[0]
        
        p_prev = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, n):
            pick = nums[i] + p_prev
            no_pick = 0 + prev

            cur = max(pick, no_pick)
            
            p_prev = prev
            prev = cur
        
        return prev