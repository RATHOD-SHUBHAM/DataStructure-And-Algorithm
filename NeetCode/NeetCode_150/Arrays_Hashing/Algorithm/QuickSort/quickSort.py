# Tc: O(nlogn) | Sc: O(logn)
def quickSort(array):
    n = len(array)

    startIdx = 0
    endIdx = n - 1

    quick(startIdx, endIdx, array)

    return array

def quick(startIdx, endIdx, array):
    if startIdx >= endIdx:
        return

    pivot = startIdx
    left = pivot + 1
    right = endIdx

    while left <= right:
        '''
            - Element larger than pivot must be to the right of pivot
            - Element smaller than pivot must be to the left of pivot
        '''
        if array[left] > array[pivot] and array[pivot] > array[right]:
            swap(left, right, array)

        if array[left] <= array[pivot]:
            left += 1

        if array[pivot] <= array[right]:
            right -= 1

    swap(pivot, right, array)

    smaller_array = (right - 1) - startIdx < endIdx - (right + 1)
    if smaller_array:
        quick(startIdx, right - 1, array)
        quick(right + 1, endIdx, array)
    else:
        quick(right + 1, endIdx, array)
        quick(startIdx, right - 1, array)


def swap(i, j, array):
    array[i], array[j] = array[j] , array[i]
        
    
