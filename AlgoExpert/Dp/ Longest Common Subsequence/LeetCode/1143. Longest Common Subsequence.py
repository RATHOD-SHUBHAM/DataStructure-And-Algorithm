'''

1143. Longest Common Subsequence
Medium


Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.


'''


# Time and Space = O(m.n)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # creating a 2 * 2 matrix
        dp = [[0 for _ in range(len(text2)+1) ] for _ in range(len(text1)+1)]
        
        # bottom up approach
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                # whenever there is a match it will be in diagonal
                # all the match will be stored in diagonal
                # so when there is a match increase the count of diagonal by one
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: # take the max value and fill in the matrix, so that the answer will travel up
                    dp[i][j] = max(dp[i+1][j] , dp[i][j+1])
        
        return dp[0][0]