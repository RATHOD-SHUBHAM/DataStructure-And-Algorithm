class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        i = m - 1
        j = n - 1

        return self.recursion(i, j, s, p)
    
    def recursion(self, i, j, s, p):
        # base case
        if i < 0 and j < 0:
            # when both string and pattern matched completely
            return True
        
        if j < 0 and i >= 0:
            # When there is some string remaining but pattern got exhausted
            return False
        
        if i < 0:
            # When string is complete
            for x in range(j+1):
                # We need to check if pattern is all * -> because * can be matched to empty string
                if p[x] != '*':  # Changed from p[j] to p[x]
                    return False
            
            return True
        
        # Logic
        if s[i] == p[j] or p[j] == '?':
            # if the character matched, or we used ? to match single character
            return self.recursion(i - 1, j - 1, s, p)
        
        elif p[j] == '*':
            # Wildcard match
            # Consider * = "" -> so we move forward
            split_1 = self.recursion(i, j-1, s, p)

            # Consider * = character at s[i]
            split_2 = self.recursion(i-1, j, s, p)
            # We dont move j-1 because we can match any number of character - so keep * to match with upcoming characters

            return split_1 or split_2
        
        else:
            # Characters didnt match
            return False