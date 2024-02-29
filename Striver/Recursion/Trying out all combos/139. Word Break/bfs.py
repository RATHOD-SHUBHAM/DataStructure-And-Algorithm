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
                # If the end point is already present - dont add again - just continue
                if end in seen:
                    continue
                
                cur_substring = s[start : end]

                if cur_substring not in wordSet:
                    continue
                
                # if the cur_substring is present in wordSet
                # add the -next substring start point- to the queue
                queue.append(end)
                # mark the start point of next substring as visited
                seen.add(end)
        
        # if start didnt match till the end
        return False