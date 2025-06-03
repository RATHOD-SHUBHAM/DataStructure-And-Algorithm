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
