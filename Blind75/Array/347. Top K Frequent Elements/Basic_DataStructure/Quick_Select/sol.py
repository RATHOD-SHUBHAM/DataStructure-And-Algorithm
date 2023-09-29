'''
    The algorithm is similar to QuickSort. 
    The difference is, instead of recurring for both sides (after finding pivot), 
    it recurs only for the part that contains the k-th smallest element. 
    
    The logic is simple, 
        * If index of the partitioned element is more than k, then we recur for the left part. 
        * If index is the same as k, we have found the k-th smallest element and we return. 
        * If index is less than k, then we recur for the right part. 
    
    This reduces the expected complexity from O(n log n) to O(n), with a worst-case of O(n^2).
'''

# Best Time : Tc: O(n) | Sc: O(1)
# Worst Time : Tc :O(n^2) | Sc: O(1)

def quickselect(array, k):
    n = len(array)
    pos = k - 1
    startIdx = 0
    endIdx = n - 1

    return sort(array, pos, startIdx, endIdx)
    
def sort(array, pos, startIdx, endIdx):
    # Quick Sort Part
    if startIdx > endIdx:
        return

    pivot = startIdx
    left = startIdx + 1
    right = endIdx

    while right >= left:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(left, right, array)

        if array[left] <= array[pivot]:
            left += 1

        if array[right] >= array[pivot]:
            right -= 1

    swap(right, pivot, array)

    # Quick Select Part
    if right == pos:
        return array[pos]
    elif right > pos:
        endIdx = right - 1
        return sort(array, pos, startIdx, endIdx)
    elif right < pos:
        startIdx = right + 1
        return sort(array, pos, startIdx, endIdx)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]