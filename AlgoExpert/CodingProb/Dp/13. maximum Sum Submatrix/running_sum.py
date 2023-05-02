# Tc and Sc: O(w * h)

import math
def maximumSumSubmatrix(matrix, size):
    # create a dp array to get running sum
    dp = runningSum(matrix)

    max_sum = -math.inf

    # traverse across the window and get the sum
    m = len(matrix)
    n = len(matrix[0])
    
    x = size - 1
    
    for i in range(x, m):
        for j in range(x, n):
            # get the running sum until here
            total_sum = dp[i][j]

            # check if there is any value that need to be subtracted
            top_border = i - size

            # check if we have value above
            if top_border >= 0:
                top_sum = dp[i - size][j]
                total_sum -= top_sum

            # check if there is any value to the left
            left_border = j - size

            if left_border >= 0:
                left_sum = dp[i][j-size]
                total_sum -= left_sum

            # if we have both top and left border - we need to add some part back
            if top_border >= 0 and left_border >= 0:
                extra_val = dp[i - size][j - size]
                total_sum += extra_val

            max_sum = max(max_sum , total_sum)

    return max_sum

def runningSum(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    # first cell - will be same as matrix
    dp[0][0] = matrix[0][0]

    # fill in first row
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + matrix[0][i]

    # fill in first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    # fill in remaing cell
    for i in range(1, m):
        for j in range(1, n):
            curVal = matrix[i][j]
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + curVal

    # print(dp)
    return dp