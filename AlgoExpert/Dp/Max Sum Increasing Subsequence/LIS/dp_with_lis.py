# Tc: O(n^2) | Sc: O(n) 
def maxSumIncreasingSubsequence(array):
    n = len(array)

    dp = [1 for _ in range(n)]
    hash_list = [None for _ in range(n)]

    for curIdx in range(1 , n):
        for prevIdx in range(curIdx):
            dontTake = 0 + dp[curIdx]
            dp[curIdx] = dontTake

            if array[curIdx] > array[prevIdx]:
                take = 1 + dp[prevIdx]
                dp[curIdx] = max(dp[curIdx] , take)
                hash_list[curIdx] = prevIdx

    maxIdx = dp.index(max(dp))
    return buildSequence(array, dp, maxIdx, hash_list)

def buildSequence(array, dp, curIdx, hash_list):
    subsequence = []
    total = 0

    while curIdx is not None:
        total += array[curIdx]
        subsequence.append(array[curIdx])

        curIdx = hash_list[curIdx]

    return [total, subsequence[::-1]]
        