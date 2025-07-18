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