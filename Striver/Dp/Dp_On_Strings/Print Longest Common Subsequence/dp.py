# Tc: O(m * n)
# Sc: O(m * n)
def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # Write your code here
    idx1 = n - 1
    idx2 = m - 1

    dp = [["" for _ in range(m+1)] for _ in range(n+1)]


    for i in range(1, n+1):
        for j in range(1, m+1):
            ## Match
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + s1[i-1] # or s2[j-1]
            else:
                ## No Match
                split_1 = dp[i-1][j]
                split_2 = dp[i][j-1]

                if len(split_1) >= len(split_2):
                    dp[i][j] = split_1
                else:
                    dp[i][j] = split_2
                
    
    return dp[n][m]
            