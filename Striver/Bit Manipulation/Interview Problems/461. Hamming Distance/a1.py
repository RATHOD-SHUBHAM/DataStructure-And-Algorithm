class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Identify the position at which bits are different
        xor = x ^ y

        # Count the bits that are different
        count = 0
        while xor >= 1:
            if xor & 1 == 1:
                count += 1
            
            xor = xor >> 1
        
        return count
    
# ----------------------------------------------------------

# Brian Kernighan’s Algorithm

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Identify the position at which bits are different
        xor = x ^ y

        # Count the bits that are different
        count = 0
        while xor != 0:
            xor = xor & (xor - 1)
            count += 1
        
        return count