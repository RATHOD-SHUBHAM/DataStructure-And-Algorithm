#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        
         # since our base case has -1, lets add a extra layer in dp represent -1
        dp = [0 for _ in range(n+1)]
        
        max_substring = float("-inf")

        for i in range(1, m+1):
            temp = [0 for _ in range(n+1)]
            for j in range(1, n+1):
                # Match: When the character matches
                if s1[i-1] == s2[j-1]: # Our index is padded, inorder to correct it , we do -1
                    temp[j] = 1 + dp[j-1]
                else:
                    # No Match: When the character doesnot matches
                    temp[j] = 0
            
            max_substring = max(max_substring, max(dp))
            dp = temp
        
        max_substring = max(max_substring, max(dp))
        return max_substring