# Tc and Sc: O(1)
# brians algorithm
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        XOR = x ^ y
        count = 0
        
        # this check the number is not zero
        # while there is atleast one 1
        while XOR:
            count += 1
            XOR = (XOR) & (XOR - 1)
        
        return count