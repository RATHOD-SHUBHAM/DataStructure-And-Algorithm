# ---------------------------------------- Using Dictionary ----------------------------------------

"""
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

The below solution works perfectly for the follow up
"""

# Tc & Sc: O(m+n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = collections.Counter(s)
        
        count_t = collections.Counter(t)

        return count_s == count_t
    
# ---------------------------------------- Using Fixed size List ----------------------------------------

# Tc and Sc: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Create a fixed array of size 26 for 'a' to 'z'
        count = [0] * 26
        
        # Increment for characters in s, decrement for characters in t
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # If all counts are 0, they're anagrams
        return all(c == 0 for c in count)
        # for c in count:
        #         if c != 0:
        #             return False
            
        #     return True