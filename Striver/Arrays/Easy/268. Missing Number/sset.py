# Tc: and Sc O(n)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        set_s = set(nums)

        for i in range(n):
            if i not in set_s:
                return i
        
        return n