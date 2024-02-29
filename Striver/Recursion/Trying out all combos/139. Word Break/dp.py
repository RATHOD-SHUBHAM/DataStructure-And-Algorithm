class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True # end index - valid base case

        for i in reversed(range(len(s))):
            # match this with every word in wordDict
            for word in wordDict:
                # check if the substring are with in the boundary
                substring_end_idx = i + len(word)
                if substring_end_idx > len(s):
                    continue
                
                substring = s[i : substring_end_idx]
                if word != substring:
                    continue
                
                # check if the other substring is valid
                if dp[substring_end_idx] == True:
                    dp[i] = True
                    break # match found so move to next index
        
        return dp[0]