def palindromePartitioningMinCuts(string):
    n = len(string)
        
    dp = [0] * (n + 1)
    dp[n] = 0 # this was the base case in recursion
    
    pali = [[None for _ in range(n)] for _ in range(n)]
    
    for i in reversed(range(n)):
        # copy the recurence
        minCost = float("inf")

        for j in range(i , n):
            # cur_string = s[i : j + 1]

            if isPalindrome(i ,j , string, pali):
                cost = 1 + dp[j+1]

                minCost = min(minCost , cost)
                
        dp[i] = minCost
    
     # -1 becasue eg: aba - it will add a cut in end
    return  dp[0] - 1

def isPalindrome(left, right, cur_string, pali):
    if pali[left][right]:
        return pali[left][right]
    
    while left < right:
        if cur_string[left] != cur_string[right]:
            pali[left][right] = False
            return pali[left][right]
        
        left += 1
        right -= 1
    
    pali[left][right] = True

    return pali[left][right]