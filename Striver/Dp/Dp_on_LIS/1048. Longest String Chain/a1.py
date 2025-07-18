class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        sorted_words = sorted(words, key = len, reverse = True)

        # Map -> word:idx
        dic = collections.defaultdict(int)
        for i in range(n):
            dic[sorted_words[i]] = i

        max_len = 1
        for i in range(n):
            cur_len = self.recursion(i, dic, sorted_words, n)
            max_len = max(max_len, cur_len)
        
        return max_len
    
    def recursion(self, idx, dic, sorted_words, n):
        # base case
        if idx == n:
            return 0
        
        max_len = 1
        x = len(sorted_words[idx])
        word = sorted_words[idx]
        for i in range(x):
            cur_word = word[:i] + word[i+1 : ] # these will capture the subset
            # Check if the subset is present in the input
            if cur_word in dic:
                # Get the idx of subset
                nxt_idx = dic[cur_word]
                cur_len = 1 + self.recursion(nxt_idx, dic, sorted_words, n)
                max_len = max(max_len, cur_len)
        
        return max_len
    
# ---------------------------- Memoization ----------------------------
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        sorted_words = sorted(words, key = len, reverse = True)

        # Map -> word:idx
        dic = collections.defaultdict(int)
        for i in range(n):
            dic[sorted_words[i]] = i

        max_len = 1
        for i in range(n):
            cur_len = self.recursion(i, {}, dic, sorted_words, n)
            max_len = max(max_len, cur_len)
        
        return max_len
    
    def recursion(self, idx, memo, dic, sorted_words, n):
        # base case
        if idx == n:
            return 0
        
        if idx in memo:
            return memo[idx]
        
        max_len = 1
        x = len(sorted_words[idx])
        word = sorted_words[idx]
        for i in range(x):
            cur_word = word[:i] + word[i+1 : ] # these will capture the subset
            # Check if the subset is present in the input
            if cur_word in dic:
                # Get the idx of subset
                nxt_idx = dic[cur_word]
                cur_len = 1 + self.recursion(nxt_idx, memo, dic, sorted_words, n)
                max_len = max(max_len, cur_len)
        
        memo[idx] = max_len
        return memo[idx]

# ---------------------------- Dynamic Programming ----------------------------
"""
The problem wants:

- Chains where each word is a predecessor of the next
- A predecessor means you can add one character to get the next word
- So chains should go from shortest to longest

"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        sorted_words = sorted(words, key = len) # Removed reverse=True - we need to process shortest to longest

        # Map -> word:idx
        dic = collections.defaultdict(int)
        for i in range(n):
            dic[sorted_words[i]] = i
        
        dp = [1] * (n)

        for idx in range(n):
            max_len = 1
            x = len(sorted_words[idx])
            word = sorted_words[idx]
            
            for i in range(x):
                predecessor = word[:i] + word[i+1 : ] # these will capture the subset

                # Check if the subset is present in the input
                if predecessor in dic:
                    # Get the idx of subset
                    nxt_idx = dic[predecessor]
                    # predecessor must come before current word in sorted order
                    if nxt_idx < idx:
                        cur_len = 1 + dp[nxt_idx]
                        max_len = max(max_len, cur_len)
            
            dp[idx] = max_len
        
        # Return max(dp) instead of dp[n-1] because the longest chain might end at any word
        return max(dp)

# ---------------------------- Optimized Using LIS ----------------------------
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

# ---------------------------- Print Longest String Chain ----------------------------
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
        hsh = [i for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if self.compare(sorted_word[j], sorted_word[i]) == True:
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
                        hsh[i] = j
        
        idx = dp.index(max(dp))
        LSC = []

        while hsh[idx] != idx:
            LSC.append(sorted_word[idx])
            idx = hsh[idx]
        
        LSC.append(sorted_word[idx])

        print(LSC[::-1])
        return max(dp)