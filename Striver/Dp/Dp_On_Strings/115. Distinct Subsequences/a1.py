# Tc: O(2^(m+n))
# Sc: O(m+n) for recursion stack space

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        i = m - 1
        j = n - 1

        return self.recursion(i, j, s,t)
    
    def recursion(self, i, j, s, t):
        # base case
        if j < 0:
            # Match found: All string in `t` was matched and exhausted
            return 1
        
        if i < 0:
            # No Match found: All string in `s` is over
            return 0
        
        # Logic
        if s[i] == t[j]:
            # Match current j with i
            split_1 = self.recursion(i - 1, j - 1, s,t)
            # Do not mathc current j with i
            split_2 = self.recursion(i-1, j, s, t)

            return split_1 + split_2
        
        else:
            # No match
            return self.recursion(i-1, j, s, t)
        
# --------------------------------- Memoization ---------------------------
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        i = m - 1
        j = n - 1

        memo = {}

        return self.recursion(i, j, memo, s,t)
    
    def recursion(self, i, j, memo, s, t):
        # base case
        if j < 0:
            # Match found: All string in `t` was matched and exhausted
            return 1
        
        if i < 0:
            # No Match found: All string in `s` is over
            return 0
        
        if (i, j) in memo:
            return memo[(i,j)]
        
        # Logic
        if s[i] == t[j]:
            # Match current j with i
            split_1 = self.recursion(i - 1, j - 1, memo, s,t)
            # Do not mathc current j with i
            split_2 = self.recursion(i-1, j, memo, s, t)

            memo[(i,j)] = split_1 + split_2

            return memo[(i,j)]
        
        else:
            # No match
            memo[(i,j)] = self.recursion(i-1, j, memo, s, t)

            return memo[(i,j)]
        

# --------------------------- Tabulation ---------------------------

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] # Adding buffer

        # base case
        for i in range(m+1):
            # j < 0 : return 1
            dp[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    # Match current j with i
                    split_1 = dp[i-1][j-1]
                    # Do not mathc current j with i
                    split_2 = dp[i-1][j]

                    dp[i][j] = split_1 + split_2
        
                else:
                    # No match
                    dp[i][j] = dp[i-1][j]

        return dp[m][n]
    
# --------------------------- Space Optimization ---------------------------

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [0 for _ in range(n+1)] # Adding buffer

        # base case
        # j < 0 : return 1
        dp[0] = 1
        
        for i in range(1, m+1):
            temp = [0 for _ in range(n+1)]
            temp[0] = 1

            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    # Match current j with i
                    split_1 = dp[j-1]
                    # Do not mathc current j with i
                    split_2 = dp[j]

                    temp[j] = split_1 + split_2
        
                else:
                    # No match
                    temp[j] = dp[j]
            
            dp = temp

        return dp[n]

# --------------------------- Single Array ---------------------------

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [0 for _ in range(n+1)] # Adding buffer

        # base case
        # j < 0 : return 1
        dp[0] = 1
        
        for i in range(1, m+1):
            for j in reversed(range(1, n+1)):
                if s[i-1] == t[j-1]:
                    # Match current j with i
                    split_1 = dp[j-1]
                    # Do not mathc current j with i
                    split_2 = dp[j]

                    dp[j] = split_1 + split_2
        
                else:
                    # No match
                    dp[j] = dp[j]

        return dp[n]