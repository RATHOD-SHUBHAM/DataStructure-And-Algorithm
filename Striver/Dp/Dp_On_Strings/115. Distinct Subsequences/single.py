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