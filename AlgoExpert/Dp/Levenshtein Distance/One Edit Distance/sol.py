class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        if len_t < len_s:
            return self.isOneEditDistance(t, s)
        
        if len_t - len_s >= 2:
            return False
        
        for i in range(len_s):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i + 1 : ] == t[i + 1 : ]
                else:
                    return s[i : ] == t[i+1 : ]
            
        
        return len_s + 1 == len_t