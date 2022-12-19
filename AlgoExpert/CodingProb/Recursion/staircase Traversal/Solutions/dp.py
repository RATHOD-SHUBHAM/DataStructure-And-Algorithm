def staircaseTraversal(height, maxSteps):
    dp = [0] * (height + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, height + 1):
        # look at previous steps
        step = 1
        while step <= maxSteps:
            dp[i] += dp[i-step]
            step += 1

    return dp[height]
