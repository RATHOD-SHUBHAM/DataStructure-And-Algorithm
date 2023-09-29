# Bucket Sort Explanation
'''
    Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups called buckets. 
    Each bucket is then sorted by using any of the suitable sorting algorithms or recursively applying the same bucket algorithm.
    Finally, the sorted buckets are combined to form a final sorted array.

'''

# Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups called buckets.

# Tc: O(nlogn) | Sc: O(nk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the freq of nums
        freq = collections.defaultdict()

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        print(freq)

# We are dividing each element in a bucker called as frequency.


# ------------------------------------------------------------------

# QuickSort Explanation

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
            

# ------------------------------------------------------------------

# QuickSelect Explanation

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