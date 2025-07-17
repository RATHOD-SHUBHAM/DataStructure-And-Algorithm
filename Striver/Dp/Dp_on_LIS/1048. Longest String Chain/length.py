class Solution:
    def compare(self, word_1, word_2):
        m = len(word_1)
        n = len(word_2)

        if n != m+1:
            return False

        i = 0
        j = 0
        mismatch = False

        while i < m and j < n:
            if word_1[i] == word_2[j]:
                i += 1
                j += 1
            else:
                if mismatch == True:
                    return False
                
                mismatch = True # found a different character
                j+=1
        
        return True
        
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)

        sorted_word = sorted(words, key = len)

        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if self.compare(sorted_word[j], sorted_word[i]) == True:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)