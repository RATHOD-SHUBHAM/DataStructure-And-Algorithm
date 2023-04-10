# Brute Force
# Tc: O(w * h* size^2) | Sc: O(1)

import math
def maximumSumSubmatrix(matrix, size):
    m = len(matrix)
    n = len(matrix[0])

    max_sum = -math.inf
    for i in range(m - size + 1):
        for j in range(n - size + 1):
            window_sum = get_window_sum(i , j, matrix, size)

            max_sum = max(max_sum , window_sum)

    return max_sum

# Tc:O(size^2)
def get_window_sum(row , col, matrix, size):
    window_sum = 0

    for i in range(row , row + size):
        for j in range(col , col + size):
            window_sum += matrix[i][j]

    # print(window_sum)
    return window_sum