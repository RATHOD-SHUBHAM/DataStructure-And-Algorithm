# Find the matching bit in the range
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0

        while left < right:
            left = left >> 1
            right = right >> 1
            count += 1
        
        # Move the one to the common place
        left = left << count
        return left