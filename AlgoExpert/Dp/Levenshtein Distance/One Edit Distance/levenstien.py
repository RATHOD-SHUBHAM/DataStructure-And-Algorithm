# Tc :O(n) 
# Sc :O(n) : string are immutable in python, hence they take extra space
class Solution:
    # Check if s can be converted to t
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        if len_t < len_s:
            return self.isOneEditDistance(t, s)
        
        if len_t - len_s > 1:
            return False
        
        for i in range(len_s):
            # if the values are same - do nothing
            if s[i] == t[i]:
                continue
                
            else:
                # Levenstien distance
                insertOne = s[i : ] == t[i+1 : ]
                deleteOne = s[i + 1 : ] == t[i : ]
                replaceOne = s[i + 1 : ] == t[ i + 1 : ]
                
                return insertOne or deleteOne or replaceOne
            
        # Everything has matched - but to have one edit - t should have one element more
        return len_s + 1 == len_t