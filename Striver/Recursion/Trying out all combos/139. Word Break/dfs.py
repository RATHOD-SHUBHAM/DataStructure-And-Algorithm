# DFS - Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        memo = {} # keep track of all the substring - valid and invalid

        valid = self.memoization(memo, wordSet, s)

        return valid
    
    def memoization(self, memo, wordSet, s):
        # if the substring is present in cache
        if s in memo:
            return memo[s]
        
        if s in wordSet:
            return True
        
        for end in range(len(s) + 1):
            cur_substring = s[ : end]

            # check if the current substring and the remaining substring are valid
            if cur_substring in wordSet and self.memoization(memo, wordSet, s[end : ]):
                memo[cur_substring] = True
                return True
            
        
        memo[s] = False

        return False

        
# Solution 2: Same method

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)

        valid = self.isValid(s, wordSet, memo)
        memo[s] = valid

        return memo[s]
    
    def isValid(self, s, wordSet, memo):
        if s in memo:
            return memo[s]
        
        if s in wordSet:
            memo[s] = True
            return memo[s]
        
        for end in range(len(s)):
            cur_substring = s[ : end]

            if cur_substring in wordSet:
                valid = self.isValid(s[end : ], wordSet, memo)

                if valid:
                    memo[s] = valid
                    return memo[s]
        
        memo[s] = False
        return memo[s]