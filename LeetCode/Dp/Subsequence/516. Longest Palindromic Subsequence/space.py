# Tc: O(n^2) | O(n)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        
        # the catch here is if we write the string in reverse order and compare the original and reversed string. We will get the LCS which will eventually be the LPS
        rs = s[ : : -1]

        
        prev = [0 for _ in range(m + 1)]
        cur = [0 for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if s[i - 1] == rs[j - 1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(cur[j-1], prev[j])
                    
            prev = [x for x in cur]
                    
        return cur[-1]