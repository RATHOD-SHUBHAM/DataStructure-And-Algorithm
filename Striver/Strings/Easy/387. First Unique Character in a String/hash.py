# Tc , Sc = O(n)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s = collections.Counter(s)

        n = len(s)

        for i in range(n):
            if count_s[s[i]] == 1:
                return i
        
        return -1