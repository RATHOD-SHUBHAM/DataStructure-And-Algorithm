# Tc and Sc: O(word1 * word2)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        idx1 = len_word1 - 1
        idx2 = len_word2 - 1
        
        memo = [[None for _ in range(len_word2)]for _ in range(len_word1)]
        
        return self.getMinimumDistance(idx1, word1, idx2, word2, memo)
    
    def getMinimumDistance(self, idx1, word1, idx2, word2, memo):
        # base case
        if idx1 == 0:
            return idx2 + 1 # + 1 because the index is 0indexed value
        
        if idx2 == 0:
            return idx1 + 1
        
        if memo[idx1][idx2] != None:
            memo[idx1][idx2]
        
        # if both the character matches - get the minimum number of operations required to convert word1 to word2.
        if word1[idx1] == word2[idx2]:
            memo[idx1][idx2] = self.getMinimumDistance(idx1 - 1, word1, idx2 - 1, word2, memo)
        else:
            # COMPARE THE REST OF THE STRING
            insertOperation = self.getMinimumDistance(idx1, word1, idx2 - 1, word2, memo)
            deleteOperation = self.getMinimumDistance(idx1 - 1, word1, idx2, word2, memo)
            replaceOperation = self.getMinimumDistance(idx1 - 1, word1, idx2 - 1, word2, memo)
            
            # 1 + compare remaining elements
            minOperation = 1 + min(insertOperation , deleteOperation, replaceOperation)
            
            memo[idx1][idx2] = minOperation
            
        return memo[idx1][idx2]