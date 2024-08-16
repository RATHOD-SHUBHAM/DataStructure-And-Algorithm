# Tc:O(n^2) | Sc:O(1)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0

        for i in range(n):
            char_set = set()

            for j in range(i, n):
                char_set.add(s[j])

                if len(char_set) >= 3:
                    count += 1
        
        return count