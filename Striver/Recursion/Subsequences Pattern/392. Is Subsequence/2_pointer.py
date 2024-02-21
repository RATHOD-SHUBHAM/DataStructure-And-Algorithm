class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)

        p = q = 0

        while p < ns and q < nt:
            if s[p] == t[q]:
                p += 1
            
            q += 1
        
        return p == ns