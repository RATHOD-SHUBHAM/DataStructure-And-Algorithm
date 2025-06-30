class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        i = m - 1
        j = n - 1

        memo = {}

        return self.recursion(i, j, memo, s, p)
    
    def recursion(self, i, j, memo, s, p):
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
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Logic
        if s[i] == p[j] or p[j] == '?':
            # if the character matched, or we used ? to match single character
            memo[(i, j)] = self.recursion(i - 1, j - 1, memo, s, p)
            return memo[(i, j)]
        
        elif p[j] == '*':
            # Wildcard match
            # Consider * = "" -> so we move forward
            split_1 = self.recursion(i, j-1, memo, s, p)

            # Consider * = character at s[i]
            split_2 = self.recursion(i-1, j, memo, s, p)
            # We dont move j-1 because we can match any number of character - so keep * to match with upcoming characters

            memo[(i, j)] = split_1 or split_2
            return memo[(i, j)]
        
        else:
            # Characters didnt match
            memo[(i, j)] = False
            return memo[(i, j)]
        
# ---------------------------- Converting to 1 based indexing ----------------------------
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        i = m
        j = n

        memo = {}

        return self.recursion(i, j, memo, s, p)
    
    def recursion(self, i, j, memo, s, p):
        # base case
        if i == 0 and j == 0:
            # when both string and pattern matched completely
            return True
        
        if j == 0 and i > 0:
            # When there is some string remaining but pattern got exhausted
            return False
        
        if i == 0:
            # When string is complete
            for x in range(j):
                # We need to check if pattern is all * -> because * can be matched to empty string
                if p[x] != '*':  # Changed from p[j] to p[x]
                    return False
            
            return True
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Logic
        if s[i-1] == p[j-1] or p[j-1] == '?':
            # if the character matched, or we used ? to match single character
            memo[(i, j)] = self.recursion(i - 1, j - 1, memo, s, p)
            return memo[(i, j)]
        
        elif p[j-1] == '*':
            # Wildcard match
            # Consider * = "" -> so we move forward
            split_1 = self.recursion(i, j-1, memo, s, p)

            # Consider * = character at s[i]
            split_2 = self.recursion(i-1, j, memo, s, p)
            # We dont move j-1 because we can match any number of character - so keep * to match with upcoming characters

            memo[(i, j)] = split_1 or split_2
            return memo[(i, j)]
        
        else:
            # Characters didnt match
            memo[(i, j)] = False
            return memo[(i, j)]