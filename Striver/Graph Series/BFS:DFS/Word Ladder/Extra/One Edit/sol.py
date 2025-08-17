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
