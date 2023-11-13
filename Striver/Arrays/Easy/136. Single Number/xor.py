# Tc : O(n) and Sc : O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        xor_n = 0
        for i in nums:
            xor_n ^= i
        
        return xor_n