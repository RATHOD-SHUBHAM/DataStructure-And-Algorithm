# Tc & Sc: O(N)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic_s = {}
        dic_t = {}

        n = len(s)

        for i in range(n):
            if s[i] in dic_s:
                if dic_s[s[i]] != t[i]:
                    return False
            if t[i] in dic_t:
                if dic_t[t[i]] != s[i]:
                    return False
            
            dic_s[s[i]] = t[i]
            dic_t[t[i]] = s[i]
        
        return True