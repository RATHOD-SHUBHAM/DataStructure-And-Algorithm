# Tc: O(n^2) | Sc: O(n) 
def maxSumIncreasingSubsequence(array):
    n = len(array)

    dp = [num for num in array]

    pointerToSubsequence = [None] * n 


    for curIdx in range(1 , n):
        for prevIdx in range(curIdx):
            if array[prevIdx] < array[curIdx] and  array[curIdx] + dp[prevIdx] > dp[curIdx]:
                dp[curIdx] = array[curIdx] + dp[prevIdx]
                pointerToSubsequence[curIdx] = prevIdx

    print("dp: ", dp)
    maxIndex = dp.index(max(dp))
    return buildSubsequence(array, pointerToSubsequence, maxIndex)

# build using the hash pointer
def buildSubsequence(array, pointerToSubsequence, curIndex):
    subseq = []
    total = 0

    while curIndex is not None:
        total += array[curIndex]
        subseq.append(array[curIndex])
        curIndex = pointerToSubsequence[curIndex]

    return (total, subseq[::-1])
        