# Tc and Sc: O(n)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        if len_s > len_t:
            return self.isOneEditDistance(t,s)
            
        if len_t - len_s >= 2:
            return False
        
        for i in range(len_s):
            # when the characters are different
            if s[i] != t[i]:
                # if s and t are of same length
                if len_s == len_t:
                    return s[i + 1 : ] == t[i + 1 : ]
                else:
                    return s[i : ] == t[i + 1 : ]
                
        
        # if s and t are same
        # string s is said to be one edit distance away if there is atleast one char difference
        return len_s + 1 == len_t