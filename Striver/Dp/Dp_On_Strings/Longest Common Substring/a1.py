#User function Template for python3

class Solution:
    def __init__(self):
        self.max_len = float('-inf')
        self.count = 0
    def longestCommonSubstr(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        
        idx1 = m-1
        idx2 = n-1
        
        self.recursion(idx1, idx2, s1, s2)
        
        return self.max_len
    
    def recursion(self, idx1, idx2, s1, s2):
        # Base case
        if idx1 < 0 or idx2 < 0:
            self.max_len = max(self.max_len, self.count)
            self.count = 0
            return
        
        # Logic
        ## Match
        if s1[idx1] == s2[idx2]:
            self.count += 1
            return self.recursion(idx1-1, idx2-1, s1, s2)
        
        # No Match

        # Store the max length found so far
        self.max_len = max(self.max_len, self.count)
        
        # Reset Count
        self.count = 0
        split_1 = self.recursion(idx1-1, idx2, s1, s2)
        
        self.count = 0
        split_2 = self.recursion(idx1, idx2-1, s1, s2)
        
        return

# ----------------- Tabulation -----------------

#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        # code here
        m = len(s1)
        n = len(s2)
        
         # since our base case has -1, lets add a extra layer in dp represent -1
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]

        # for i in range(m+1):
        #     dp[i][0] = 0
        
        # for j in range(n+1):
        #     dp[0][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                # Match: When the character matches
                if s1[i-1] == s2[j-1]: # Our index is padded, inorder to correct it , we do -1
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # No Match: When the character doesnot matches
                    dp[i][j] = 0
        
        max_substring = float("-inf")
        for i in range(1, m+1):
            cur_max = max(dp[i])
            max_substring = max(max_substring, cur_max)
        
        return max_substring
    
# ----------------- Space Optimization -----------------

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