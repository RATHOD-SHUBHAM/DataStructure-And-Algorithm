class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Identify the position at which bits are different
        xor_result = start ^ goal
        
        # Count the bits that are different
        count = 0
        while xor_result:
            count += xor_result & 1

            xor_result >>= 1
        
        return count