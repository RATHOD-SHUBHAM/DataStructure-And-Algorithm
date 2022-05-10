# Time = O(n^2)
# Space = O(n^2)

import math
class Solution:
    def minCut(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        # make all the diagonal True
        for i in range(len(s)):
            dp[i][i] = True
        
        # Go through sub array
        for length in range(2, len(s) + 1): # we need 2 ele to make a subarray
            for i in range(0, len(s) - length + 1):
                j = i + length - 1 # because index start from 0
                
                # if there are 2 element in subarray
                if length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        # print(dp)
        
        minCuts = [-math.inf for _ in range(len(s))]
        
        for i in range(len(s)):
            if dp[0][i]:
                minCuts[i] = 0
            else:
                # prevCut + 1
                minCuts[i] = minCuts[i-1] + 1
                
                # check if there is a palindrome present
                for j in range(1,i):
                    if dp[j][i] and minCuts[j-1]  + 1 < minCuts[i]: 
                        minCuts[i] = minCuts[j-1] + 1
        return minCuts[-1]