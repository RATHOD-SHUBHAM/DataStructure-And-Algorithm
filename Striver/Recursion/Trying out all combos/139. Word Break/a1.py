# 1. Recursion - TLE

# This will Time out

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        # Helper Function ---------
        def isValid(start):
            # base case
            if start == len(s):
                return True
            
            for end in range(start, len(s) + 1):
                cur_substring = s[start : end]
                # print(cur_break)

                if cur_substring in wordSet:
                    valid = isValid(end)

                    if valid == True:
                        return True
            
            return False


        # Main Function ---------
        valid = isValid(0)

        if valid == True:
            return True
        
        return False
    
# ---------------------------------------------------------------------------------------------------

# 2. BFS: Improve the time complexity by keeping track of visted substring

from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        queue = deque([0]) # append start index
        
        # keep track of endpoints
        seen = set()

        while queue:
            start = queue.pop()

            if start == len(s):
                return True
            
            for end in range(start, len(s) + 1):
                
                cur_substring = s[start : end]

                if cur_substring not in wordSet:
                    continue
                
                # If the end point is already present - dont add again - just continue
                if end in seen:
                    continue
                
                # if the cur_substring is present in wordSet
                # add the -next substring start point- to the queue
                queue.append(end)
                # mark the start point of next substring as visited
                seen.add(end)
        
        # if start didnt match till the end
        return False

# ---------------------------------------------------------------------------------------------------

# 3. DFS - Memoization
    
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

# ---------------------------------------------------------------------------------------------------

# 4. Dp

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


