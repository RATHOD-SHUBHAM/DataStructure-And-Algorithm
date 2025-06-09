# Tc: O(n)
# Sc: O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        # Track the range of possible open parentheses count
        min_open = 0  # minimum possible open parens -> best case scenario
        max_open = 0  # maximum possible open parens -> worst case scenario
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1

            elif char == ')':
                min_open -= 1
                max_open -= 1
            
            else:  # char == '*'
                # char - 1, char + 1, or char (empty string) -> so range = [-1, 0, +1]
                min_open -= 1  # treat as ')'
                max_open += 1  # treat as '('
            
            # If max_open becomes negative, we have too many ')' 
            if max_open == -1:
                return False
            
            # min_open should never go below 0
            if min_open == -1:
                min_open = 0

        
        # At the end, we need min_open to be 0 or less
        # (meaning it's possible to have 0 open parens)
        return min_open == 0