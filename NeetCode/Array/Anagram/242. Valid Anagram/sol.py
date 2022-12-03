# Tc and Sc: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = {}
        counter_t = {}
        
        for i in range(len(s)):
            if s[i] not in counter_s:
                counter_s[s[i]] = 0
                
            counter_s[s[i]] += 1
            
        for i in range(len(t)):
            if t[i] not in counter_t:
                counter_t[t[i]] = 0
                
            counter_t[t[i]] += 1
        
        # print(counter_s, counter_t)
        return counter_s == counter_t