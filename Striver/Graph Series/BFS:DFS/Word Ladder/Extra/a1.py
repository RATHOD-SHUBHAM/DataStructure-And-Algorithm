# At most One Edit Distance

class Solution:
    def isOneEditAway(self, word1: str, word2: str) -> bool:
        m, n = len(word1), len(word2)
        
        # If length difference > 1, can't be one edit away
        if abs(m - n) > 1:
            return False
        
        # Ensure word1 is the shorter one
        if m > n:
            word1, word2 = word2, word1
            m, n = n, m
        
        i = j = 0
        edits = 0
        
        while i < m and j < n:
            if word1[i] != word2[j]:
                if edits == 1:  # Already found a difference before
                    return False
                edits += 1
                
                if m == n:
                    # Same length -> must be replacement
                    i += 1
                    j += 1
                else:
                    # Different length -> must be insertion in longer word
                    j += 1
            else:
                i += 1
                j += 1
        
        # If we reached end, but longer word has one extra char
        if j < n or i < m:
            edits += 1
        
        return edits <= 1

if __name__ == "__main__":
    s = Solution()
    print(s.isOneEditAway("hit", "hot"))   # True  (replace 'i' -> 'o')
    print(s.isOneEditAway("hitt", "hot"))  # False (diff > 1 edit)
    print(s.isOneEditAway("cat", "cats"))  # True  (one insertion)
    print(s.isOneEditAway("cat", "cut"))   # True  (one replacement)
    print(s.isOneEditAway("cat", "dog"))   # False (3 replacements)
    print(s.isOneEditAway("", "a"))        # True  (one insertion)


# ------------------------- Exactly One Edit Distance -------------------------
# Tc: O(m)
# Sc: O(1)

# Exactly One Edit Distance

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        # Make sure second value is greater than first
        if m > n:
            return self.isOneEditDistance(t, s)
        
        # if there difference is more than 1, we will need more than one edit to make both the string same
        if n - m > 1:
            return False
        
        for i in range(m):
            if s[i] != t[i]:
                # If there are of same len
                if m == n:
                    return s[i+1: ] == t[i+1 : ]
                else:
                    return s[i : ] == t[i+1 : ]
        
        # if m is exhausted and n is remaininf, then we got to make sure , they are away by 1 char
        return m+1 == n