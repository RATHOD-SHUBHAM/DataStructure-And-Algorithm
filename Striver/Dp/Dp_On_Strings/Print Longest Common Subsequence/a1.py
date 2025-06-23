# Tc: O(2^m * 2^n) = O(2^(m+n))
# Sc: O(m * n)

def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # Write your code here
    idx1 = n - 1
    idx2 = m - 1

    return recursion(idx1, idx2, s1, s2)

def recursion(idx1, idx2, text1, text2):
    # Base case
    if idx1 < 0 or idx2 < 0:
        return ""
    
    # Logic
    LCS = "" # Global variable modification: If we try to modify a global LCS string from within the recursion, it wont work because strings are immutable in Python.
    ## Match
    if text1[idx1] == text2[idx2]:
        """
        If we add text[idx] first then, we are adding the current character first, then the result from recursion, which builds the string backwards.
        LCS += text1[idx1] # or text2[idx1]
        """
        LCS += recursion(idx1-1, idx2-1, text1, text2)
        LCS += text1[idx1]
        return LCS
    
    ## No Match
    split_1 = recursion(idx1-1, idx2, text1, text2)
    split_2 = recursion(idx1, idx2-1, text1, text2)

    if len(split_1) >= len(split_2):
        LCS += split_1
    else:
        LCS += split_2
    
    return LCS

# --------------- Memoization ---------------
def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # Write your code here
    idx1 = n - 1
    idx2 = m - 1

    memo = {}

    return recursion(idx1, idx2, memo, s1, s2)

def recursion(idx1, idx2, memo, text1, text2):
    # Base case
    if idx1 < 0 or idx2 < 0:
        return ""
    
    if (idx1, idx2) in memo:
        return memo[(idx1, idx2)]
    
    # Logic
    LCS = "" # Global variable modification: If we try to modify a global LCS string from within the recursion, it wont work because strings are immutable in Python.
    ## Match
    if text1[idx1] == text2[idx2]:
        """
        If we add text[idx] first then, we are adding the current character first, then the result from recursion, which builds the string backwards.
        LCS += text1[idx1] # or text2[idx1]
        """
        LCS += recursion(idx1-1, idx2-1, memo, text1, text2)
        LCS += text1[idx1]
        memo[(idx1, idx2)] = LCS
        return memo[(idx1, idx2)]
    
    ## No Match
    split_1 = recursion(idx1-1, idx2, memo, text1, text2)
    split_2 = recursion(idx1, idx2-1, memo, text1, text2)

    if len(split_1) >= len(split_2):
        LCS += split_1
    else:
        LCS += split_2
    
    memo[(idx1, idx2)] = LCS
    return memo[(idx1, idx2)]

# --------------- Tabulation ---------------
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

# --------------- Space Optimization ---------------
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
            