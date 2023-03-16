def maxSumIncreasingSubsequence(array):
    n = len(array)
    
    # keep track of max sum up until that current element
    dp_sum = array[:] #copy of array

    for i in range(1, n):
        # traverse and find sum upto current element
        for j in range(i):
            # if current number is greater that previous element - only then it is a subsequence
            if array[j] < array[i]:
                # if the input is a negative number
                # sum should always increase, but for negative number sum decreases
                if dp_sum[j] + array[i] >= dp_sum[i]:
                    dp_sum[i] = dp_sum[j] + array[i]

    print(dp_sum)