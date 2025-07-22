class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        isPali = [[False for _ in range(n)] for _ in range(n)]

        # for single character
        for i in range(n):
            isPali[i][i] = True
        
        # for 2 characters
        for i in range(n-1):
            if s[i] == s[i+1]:
                isPali[i][i+1] = True
        
        # for 3 or more characters
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and isPali[i+1][j-1] == True:
                    isPali[i][j] = True


        # Logic
        dp = [-1 for _ in range(n+1)]
        
        for i in reversed(range(0,n)):
            
            min_cuts = math.inf
            for j in range(i, n):
                
                # cur_str = s[i: j+1]

                if isPali[i][j] == True:
                    cur_cost = 1 + dp[j+1]
                    min_cuts = min(min_cuts, cur_cost)
            
            dp[i] = min_cuts
        
        return dp[0]