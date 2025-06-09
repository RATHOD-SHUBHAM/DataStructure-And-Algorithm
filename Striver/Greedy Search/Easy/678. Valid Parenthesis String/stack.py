# Tc: O(n)
# Sc: O(n)

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        open_para = [] # keep track of open parantheses
        ast = [] # keep track of asterisk3

        for i in range(n):
            if s[i] == '(':
                open_para.append(i)
            elif s[i] == '*':
                ast.append(i)
            else:
                if open_para:
                    open_para.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
        
        while open_para and ast:
            para = open_para.pop()
            at = ast.pop()

            # Check if open para occured before *
            if para > at:
                return False
        
        return True if not open_para else False