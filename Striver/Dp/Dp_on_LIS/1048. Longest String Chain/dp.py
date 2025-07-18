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