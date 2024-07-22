'''
    Skip the starting opening bracket from adding to result.
    
    Append will only append the center brackets avoiding the outer most bracket
'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_bracket_count = 0
        res = []

        for i in s:
            if i == ')':
                open_bracket_count -= 1
            
            if open_bracket_count > 0:
                res.append(i)
            
            if i == "(":
                open_bracket_count += 1
        
        return "".join(res)