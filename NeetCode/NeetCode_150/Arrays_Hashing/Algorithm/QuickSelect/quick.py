# Tc: O(nlogn) | O(logn)

def quickselect(array, k):
    # Write your code here.
    n = len(array)

    k = k - 1

    startIdx = 0
    endIdx = n - 1

    return quick(startIdx, endIdx, array, k)

def quick(startIdx, endIdx, array, k):
    # QuickSort Section
    # If there is only element in array
    if startIdx > endIdx:
        return

    pivotIdx = startIdx
    left = pivotIdx + 1
    right = endIdx

    while left <= right:
        # place smaller value to left of pivot and larger value to right of pivot
        if array[left] > array[pivotIdx] and array[pivotIdx] > array[right]:
            swap(left, right , array)

        if array[left] <= array[pivotIdx]:
            left += 1

        if array[right] >= array[pivotIdx]:
            right -= 1

    swap(pivotIdx, right, array)

    # QuickSelect Section
    if right == k:
        return array[right]
    elif right > k:
        endIdx = right - 1
        return quick(startIdx, endIdx, array, k)
    else:
        startIdx = right + 1
        return quick(startIdx, endIdx, array, k)


def swap(i, j, array):
    array[i] , array[j] = array[j] , array[i]