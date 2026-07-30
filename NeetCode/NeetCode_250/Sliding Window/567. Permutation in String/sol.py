class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False
        
        left = 0
        right = m - 1

        need = collections.Counter(s1)

        while right < n:
            # Create a window of size m for s2 and check if it is a permutation of s1
            ele = s2[left : right + 1] # rebuild the array => o(m*n)

            if collections.Counter(ele) == need:
                return True
            
            else:
                left += 1
                right += 1
        
        return False

# ===================================================================

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False
        
        counter_1 = [0] * 26 # fixed target profile (letter counts needed from s1)
        counter_2 = [0] * 26 # letter counts of the CURRENT window in s2 (size m, slides over s2)

        # Build initial window: first m characters of s1 and s2
        for i in range(m):
            idx_1 = ord(s1[i]) - ord('a')
            idx_2 = ord(s2[i]) - ord('a')

            counter_1[idx_1] += 1
            counter_2[idx_2] += 1
        
        if counter_1 == counter_2: # Check if the very first window already matches
            return True
        
        # Slide the window one character at a time across the rest of s2.
        for i in range(m, n):
            # remove the left element
            left_idx = ord(s2[i - m]) - ord('a')
            counter_2[left_idx] -= 1

            # add the right element
            right_idx = ord(s2[i]) - ord('a')
            counter_2[right_idx] += 1

            # compare current window's letter-count profile to s1's
            if counter_1 == counter_2:
                return True
        
        return False




