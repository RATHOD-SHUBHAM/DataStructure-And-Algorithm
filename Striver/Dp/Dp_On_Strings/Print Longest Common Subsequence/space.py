# Tc: O(m * n)
# Sc: O(m)
def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # Write your code here
    idx1 = n - 1
    idx2 = m - 1

    dp = ["" for _ in range(m+1)]


    for i in range(1, n+1):
        temp = ["" for _ in range(m+1)]
        
        for j in range(1, m+1):
            ## Match
            if s1[i-1] == s2[j-1]:
                temp[j] = dp[j-1] + s1[i-1] # or s2[j-1]
            else:
                ## No Match
                split_1 = dp[j]
                split_2 = temp[j-1]

                if len(split_1) >= len(split_2):
                    temp[j] = split_1
                else:
                    temp[j] = split_2
        
        dp = temp
        
    return dp[m]
            