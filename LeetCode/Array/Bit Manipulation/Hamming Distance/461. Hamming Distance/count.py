# Tc and Sc: O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        XOR = x ^ y
        return bin(XOR).count("1")