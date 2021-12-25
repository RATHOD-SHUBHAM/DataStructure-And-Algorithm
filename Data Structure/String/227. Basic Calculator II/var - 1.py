# Time = O(n)
# Space = O(n) 
# s + '+' essentially created another string of length n+1, so I would argue this is more like O(n) time and O(n) space
# Dont forget the Bodmas rule

class Solution:
    def calculate(self, s: str) -> int:
        inner, outer, result,  = 0, 0, 0, 
        opt = '+' # previous Operator
        
        for c in s + '+': # s + '+' essentially created another string of length n+1, so I would argue this is more like O(n) time and O(n) space
            if c == ' ': 
                continue
            if c.isdigit():
                inner = 10 * inner + int(c)
                continue
            if opt == '+':
                result += outer
                outer = inner
            elif opt == '-':
                result += outer
                outer = -inner
            elif opt == '*':
                outer = outer * inner
            elif opt == '/':
                outer = int(outer / inner)
            inner, opt = 0, c
        return result + outer