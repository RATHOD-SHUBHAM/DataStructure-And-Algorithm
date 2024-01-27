def countInversions(array):
    if len(array) <= 1:
        return 0

    startIdx = 0
    endIdx = len(array) # go upto the end, but do not use the end.

    return mergeSort(array, startIdx, endIdx)

def mergeSort(array, startIdx, endIdx):
    if endIdx - startIdx <= 1:
        return 0

    mid = startIdx + (endIdx - startIdx) // 2

    # we are not breaking the array, we are using index as reference
    leftArray = mergeSort(array, startIdx, mid)  # go upto mid, but do not use mid.
    rightArray = mergeSort(array, mid, endIdx)  # go upto the end, but do not use the end.

    inversions = inversionCount(array, startIdx, mid, endIdx)

    no_of_inversions = inversions + leftArray + rightArray

    return no_of_inversions

def inversionCount(array, startIdx, mid, endIdx):
    sortedArray = []

    i = startIdx
    j = mid

    inversions = 0

    while i < mid and j < endIdx:
        if array[i] <= array[j]:
            sortedArray.append(array[i])
            i += 1
        else:
            # compute the no of inversions
            inversions += mid - i
            sortedArray.append(array[j])
            j += 1

    # add the remaing element to sorted array
    sortedArray += array[i : mid] + array[j : endIdx]

    # place the value in correct position of actual array
    for idx, num in enumerate(sortedArray):
        array[startIdx + idx] = num

    return inversions
