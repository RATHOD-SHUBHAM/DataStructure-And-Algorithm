'''
Check if the number is negative:
If the number is negative, we add 2^bits to it to get its positive representation within the specified number of bits.
'''
class Solution:
    def __init__(self):
        self.hex_values = '0123456789abcdef'

    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Handling Negative Number
        if num < 0:
            num = (1 << 32) + num # (2 ** 32) + num
        
        base_16 = ""
        while num > 0:
            remainder = num % 16
            base_16 += self.hex_values[remainder]
            num = num // 16
        
        base_16 = base_16[::-1]
        return base_16

# ------------------------------------------------------------

class Solution:
    def __init__(self):
        self.hexa = '0123456789abcdef'
        
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        if num < 0:
            bit_width = 32
            num = (1 << bit_width) + num
        
        base_16 = ""
        while num >= 16:
            base_16 += self.hexa[num % 16]
            num = num // 16
        
        base_16 += self.hexa[num]
        return base_16[::-1]