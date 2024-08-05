# Tc = O(n) | Sc = O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s = [0] * 26

        n = len(s)

        for i in range(n):
            count_s[ord(s[i]) - ord('a')] += 1
        
        for i in range(n):
            if count_s[ord(s[i]) - ord('a')] == 1:
                return i
        
        return -1