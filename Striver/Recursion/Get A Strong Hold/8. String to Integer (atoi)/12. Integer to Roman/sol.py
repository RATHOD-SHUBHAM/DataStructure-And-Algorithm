# Tc: O(n) | Sc: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        rules = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10),("XL", 40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)]

        n = len(rules)

        roman = ""

        for i in reversed(range(n)):
            sym, val = rules[i]

            count = num // val

            if count == 0:
                continue
            
            symbol = sym * count
            roman += symbol

            num = num % val
        
        return roman