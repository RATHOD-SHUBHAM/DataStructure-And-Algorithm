# Tc: O(2^(m+n))
# Sc: O(m+n) for recursion stack space

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        i = m - 1
        j = n - 1

        return self.recursion(i, j, s,t)
    
    def recursion(self, i, j, s, t):
        # base case
        if j < 0:
            # Match found: All string in `t` was matched and exhausted
            return 1
        
        if i < 0:
            # No Match found: All string in `s` is over
            return 0
        
        # Logic
        if s[i] == t[j]:
            # Match current j with i
            split_1 = self.recursion(i - 1, j - 1, s,t)
            # Do not mathc current j with i
            split_2 = self.recursion(i-1, j, s, t)

            return split_1 + split_2
        
        else:
            # No match
            return self.recursion(i-1, j, s, t)