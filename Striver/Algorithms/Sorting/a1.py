# Bubble Sort ------------------------------------------

# Tc: O(n^2) | Sc: O(1)

def bubbleSort(array):
    n = len(array)

    # Traverse all element
    for _ in range(n):
        
        # Choose and Place the Current Larger element in right place
        for i in range(n-1):
            
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]


    return array
                
# Insertion Sort ------------------------------------------

# Tc: O(n^2) | Sc: O(1)

def insertionSort(array):
    n = len(array)

    # Loop throught the array
    for i in range(n):
        j = i

        # Check if predecessor is smaller than current value
        while j > 0 and array[j] < array[j-1]:
            # Swap
            array[j-1], array[j] = array[j], array[j-1]

            j -= 1

    return array


# Selection Sort ------------------------------------------

# Tc: O(n^2) | Sc: O(n)
def selectionSort(array):
    n = len(array)

    # traverse and place the min val in right place
    for i in range(n):
        
        # Select the min value
        min_val = array[i]

        for j in range(i + 1, n):

            cur_val = array[j]
            
            # If the current val < min_val, push it in front of current val
            if min_val > cur_val:

                min_val = cur_val
                
                array[i] , array[j] = array[j] , array[i]

    return array
                

# Quick Sort ------------------------------------------       

# Tc: O(n^2) | Sc: O(logn)         
                
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

        
# bucket Sort ------------------------------------------  

# Bucket Sort - Because the answer is guranted to be unique
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Get count of numbers
        counter = collections.Counter(nums)
        # print(counter)

        # Step 2: add them to frequency table
        # Even if each number occurs one time. length of this list will be equal to len(nums)
        freq_lst = [[] for _ in range(len(nums) + 1)]
        # print(freq_lst)

        for num , count in counter.items():
            freq_lst[count].append(num)
        print(freq_lst)

        # step 3: get top k elemennt
        top_k = []
        for i in reversed(range(len(freq_lst))):
            for ele in freq_lst[i]:
                top_k.append(ele)
            
            if len(top_k) == k:
                break
        
        return top_k


# Heap Sort ------------------------------------------  

# Tc: O(nlog(n)) | Sc: O(1)

class maxHeap:

    def buildHeap(self, array):
        endIdx = len(array) - 1
        parentIdx = (endIdx - 1) // 2

        for curIdx  in reversed(range(parentIdx + 1)):
            self.siftDown(curIdx, endIdx, array)

        return array

    def siftDown(self, curIdx, endIdx, array):
        # Child One Idx = (i * 2) + 1
        childOneIdx = (curIdx * 2) + 1

        while childOneIdx <= endIdx:
            # Child Two Idx = (i * 2) + 2
            childTwoIdx = (curIdx * 2) + 2

            if childTwoIdx > endIdx:
                childTwoIdx = -1

            # Get the smallest child
            if childTwoIdx != -1 and array[childTwoIdx] > array[childOneIdx]:
                childToSwap = childTwoIdx
            else:
                childToSwap = childOneIdx

            # Compare and swap with parent idx
            if array[childToSwap] > array[curIdx]:
                self.swap(childToSwap, curIdx, array)
                
                # rearrange pointers
                curIdx = childToSwap

                childOneIdx = (curIdx * 2) + 1
            
            else:
                break

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

def heapSort(array):
    maxheap = maxHeap()

    maxheap.buildHeap(array)

    # print(array)

    # Now the first element is the greatest element
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array) # largest element is in its correct place
        # print(array)
        
        maxheap.siftDown(0, endIdx - 1, array) # bring up the next laregst element to the top
        # print(array)

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]