# Prev Number: There can be only one inflation point

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        count = 0

        for i in range(n):
            prev_idx = (i-1) % n

            if nums[prev_idx] > nums[i]:
                count += 1
            
            if count > 1:
                return False
        
        return True