class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        i = m - 1
        j = n - 1

        memo = {}

        return self.recursion(i, j, memo, s,t)
    
    def recursion(self, i, j, memo, s, t):
        # base case
        if j < 0:
            # Match found: All string in `t` was matched and exhausted
            return 1
        
        if i < 0:
            # No Match found: All string in `s` is over
            return 0
        
        if (i, j) in memo:
            return memo[(i,j)]
        
        # Logic
        if s[i] == t[j]:
            # Match current j with i
            split_1 = self.recursion(i - 1, j - 1, memo, s,t)
            # Do not mathc current j with i
            split_2 = self.recursion(i-1, j, memo, s, t)

            memo[(i,j)] = split_1 + split_2

            return memo[(i,j)]
        
        else:
            # No match
            memo[(i,j)] = self.recursion(i-1, j, memo, s, t)

            return memo[(i,j)]