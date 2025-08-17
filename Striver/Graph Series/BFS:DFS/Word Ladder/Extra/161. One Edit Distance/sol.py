# Tc: O(m)
# Sc: O(1)

# Exactly One Edit Distance

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        # Make sure second value is greater than first
        if m > n:
            return self.isOneEditDistance(t, s)
        
        # if there difference is more than 1, we will need more than one edit to make both the string same
        if n - m > 1:
            return False
        
        for i in range(m):
            if s[i] != t[i]:
                # If there are of same len
                if m == n:
                    return s[i+1: ] == t[i+1 : ]
                else:
                    return s[i : ] == t[i+1 : ]
        
        # if m is exhausted and n is remaininf, then we got to make sure , they are away by 1 char
        return m+1 == n