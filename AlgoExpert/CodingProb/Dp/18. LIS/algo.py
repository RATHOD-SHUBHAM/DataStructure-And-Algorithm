# Tc: O(n^2) | Sc: O(n)
def longestIncreasingSubsequence(array):
    n = len(array)

    dp = [1] * n
    hash_list = [None] * n

    for curIdx in range(1, n):
        for prevIdx in range(0, curIdx):

            maxLen = float("-inf")
            
            dontTake = 0 + dp[curIdx]
            maxLen = dontTake
        
            if array[curIdx] > array[prevIdx] and dp[curIdx] < 1 + dp[prevIdx]:
                Take = 1 + dp[prevIdx]
                maxLen = max(Take, maxLen)
                hash_list[curIdx] = prevIdx

            dp[curIdx] = maxLen

    return buildSubsequence(dp, hash_list, array)

def buildSubsequence(dp, hash_list, array):
    seq = []

    curIdx = dp.index(max(dp))

    while curIdx is not None:
        seq.append(array[curIdx])

        curIdx = hash_list[curIdx]

    return seq[::-1]