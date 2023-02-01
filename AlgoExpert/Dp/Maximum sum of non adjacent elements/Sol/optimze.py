# optimized
# Tc: O(n) | Sc: O(1)
def maxSubsetSumNoAdjacent(array):
    # base case
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    # code
    n = len(array)
    # previously while building the Dp array we observed that
    # we only needed 2 value ie (i-1) , (i-2) - so we can store just these 2 values in a variable, rather than a array
    non_adj_val = array[0]
    adj_val = max(array[0], array[1])

    for i in range(2, n):
        # max value till adjacent node , or max value + curr val of non adj node
        curVal = max(adj_val , non_adj_val + array[i])
        # for the next idx - curVal will be adj_val
        non_adj_val = adj_val
        adj_val = curVal

    return adj_val # last val from curVal will be stored in adj_val