# Tc and Sc: O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        XOR = x ^ y
        # print(XOR)
        # print(bin(XOR))
        # print(type(XOR))
        # print(type(bin(XOR)))
        count = 0
        
        while XOR:
            # 1 & 1 = 1 = True
            if XOR & 1:
                count += 1
            
            # keep moving right or left
            XOR = XOR >> 1
        
        return count