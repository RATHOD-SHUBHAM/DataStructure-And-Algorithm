class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        isNegative = False
        if num < 0:
           isNegative = True
        
        num = abs(num)
        base_7 = ""
        
        while num > 0:
            remainder = num % 7
            base_7 += str(remainder)
            num = num // 7
        
        base_7 = base_7[::-1]
        return "-"+base_7 if isNegative else base_7


# ------------------------------------------------------------

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        isNegative = False
        if num < 0:
            isNegative = True
        
        num = abs(num)
        
        bin_str = ""
        while num >= 7:
            bin_str += str(num % 7)
            num = num // 7
        
        bin_str += str(num)
        
        return "-" + bin_str[::-1] if isNegative else bin_str[::-1]