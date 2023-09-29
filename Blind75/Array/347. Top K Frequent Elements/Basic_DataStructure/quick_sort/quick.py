'''
    QuickSort is a sorting algorithm based on the Divide and Conquer algorithm 
    that picks an element as a pivot and 
    partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.
'''


# Best Tc: O(nlogn) | Sc: O(logn)
# Worst Tc: O(n^2) | Sc: O(logn)

def quickSort(array):
    n = len(array)
    startIdx = 0
    endIdx = n - 1

    # perform quick sort
    sort(array, startIdx, endIdx)

    return array

def sort(array, startIdx, endIdx):
    
    # Base Case eg: [1,2]
    if startIdx >= endIdx:
        return

    pivot = startIdx # first element
    left = startIdx + 1
    right = endIdx

    '''
        Trying to place pivot in coorect position
        all element to left -> smaller than pivot
        all element to right -> greater than pivot
    '''
    # Eg: [1,2]
    while right >= left:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(left, right, array)

        # Move pointers if left < pivot < right
        if array[left] <= array[pivot]:
            left += 1

        if array[right] >= array[pivot]:
            right -= 1

    swap(right, pivot, array)

    # Get the smaller unsorted array
    smaller_array = (right - 1) - startIdx < endIdx - (right + 1)

    if smaller_array:
        sort(array, startIdx, right - 1) # First Half
        sort(array, right + 1, endIdx) # Second Half
    else:
        sort(array, right + 1, endIdx) # Second Half
        sort(array, startIdx, right - 1) # First Half

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
            
