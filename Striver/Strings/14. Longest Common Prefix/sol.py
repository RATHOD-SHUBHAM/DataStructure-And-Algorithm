# Tc: O(n) | Sc: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0]) # this can any string

        i = 0

        res = ""

        while i < n:
            for s in strs:
                '''
                    if out of bound or character doesnot match
                '''
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            
            res += strs[0][i]
            i += 1
        
        return res