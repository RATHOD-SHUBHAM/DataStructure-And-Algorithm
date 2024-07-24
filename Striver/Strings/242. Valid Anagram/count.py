import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        return s_count == t_count