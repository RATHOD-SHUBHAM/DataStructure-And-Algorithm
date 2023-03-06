# Tc and Sc: O(exponential)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        idx1 = len_word1 - 1
        idx2 = len_word2 - 1
        
        return self.getMinimumDistance(idx1, word1, idx2, word2)
    
    def getMinimumDistance(self, idx1, word1, idx2, word2):
        # base case
        if idx1 == 0:
            return idx2 + 1 # + 1 because the index is 0indexed value
        
        if idx2 == 0:
            return idx1 + 1
        
        # if both the character matches - get the minimum number of operations required to convert word1 to word2.
        if word1[idx1] == word2[idx2]:
            return self.getMinimumDistance(idx1 - 1, word1, idx2 - 1, word2)
        else:
            insertOperation = self.getMinimumDistance(idx1, word1, idx2 - 1, word2)
            deleteOperation = self.getMinimumDistance(idx1 - 1, word1, idx2, word2)
            replaceOperation = self.getMinimumDistance(idx1 - 1, word1, idx2 - 1, word2)
            
            # # 1 + compare remaining elements
            minOperation = 1 + min(insertOperation , deleteOperation, replaceOperation)
            
            return minOperation