def numberOfBinaryTreeTopologies(n):
    dp = [1] * (n + 1)

    # break n into small subproblem 
    for small_n in range(1 , n + 1):
        topo_count = 0
        
        for leftTree in range(small_n):
            rightTree = small_n - 1 - leftTree
            topo_count += dp[leftTree] * dp[rightTree]
        
        dp[small_n] = topo_count
    
    return dp[-1] if n > 0 else dp[0]