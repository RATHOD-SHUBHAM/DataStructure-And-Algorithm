def quickSort(array):
    n = len(array)

    start = 0
    end = n - 1

    quick(array, start, end)

    return array

def quick(array, start, end):
    if start >= end:
        return

    # Pointers
    pivot = start
    left = start + 1
    right = end
    

    '''
        All element to left of pivot should be smaller than pivot.
        All element to the right of pivot should be greater than pivot.
    '''
    while left <= right:
        
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(array, left, right)

        if array[left] <= array[pivot]:
            left += 1

        if array[right] >= array[pivot]:
            right -= 1

    # Place pivot at correct position
    swap(array, pivot, right)

    # Get the smaller subarray
    small_sub_array = right - 1 - start < end - right + 1

    if small_sub_array:
        quick(array, start, right - 1)
        quick(array, right + 1, end)
    else:
        quick(array, right + 1, end)
        quick(array, start, right - 1)

def swap(array, i , j):
    array[i], array[j] = array[j], array[i]
        