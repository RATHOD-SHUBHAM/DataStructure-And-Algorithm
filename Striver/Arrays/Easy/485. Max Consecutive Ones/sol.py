# Tc: O(n) | Sc: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        max_ones = 0
        for i in range(n):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                max_ones = max(max_ones , count)
        
        return max_ones