# Tc: max(O(w1), O(w2)) | Sc: O(1) - if we dont consider op string else O(w1 + w2)

"""
Three req:
1. start with word1
2. Merge alternating order if string
3. Append additional letter to end
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1) # Tc:O(w1)
        w2 = len(word2) #Sc: O(w2)

        i = j = 0

        op_st = ""

        while i < w1 and j < w2:
            # Merge alternate
            op_st += word1[i] # Start with word_1
            op_st += word2[j]

            i += 1
            j += 1
        
        # Extra, append in end
        if i == w1:
            op_st += word2[j : ]
        
        if j == w2:
            op_st += word1[i : ]
        
        return op_st
