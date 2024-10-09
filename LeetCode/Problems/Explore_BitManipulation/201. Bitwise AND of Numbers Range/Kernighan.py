# Find the matching bit in the range
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1) # turn off the right most bit
        
        return right