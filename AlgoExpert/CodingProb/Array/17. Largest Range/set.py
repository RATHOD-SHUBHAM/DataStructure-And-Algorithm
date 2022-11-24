# 128 : Longest Consequtive Subsequence question leetcode
# Tc and Sc = O(n)
# best solution

import math
def largestRange(array):
    longestRange = -math.inf
    op = [-1, -1]
    num_set = set(array) # look up is  O(1)

    for num in array:
        # check if this the start range
        if num - 1 not in num_set:
            cur_range = 1
            start_range = end_range = num

            while end_range + 1 in num_set:
                end_range += 1
                cur_range += 1

            if cur_range > longestRange:
                longestRange = cur_range
                op[0] = start_range
                op[1] = end_range

    return op
