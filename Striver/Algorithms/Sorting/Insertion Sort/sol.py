'''
To sort an array of size N in ascending order 
    - Iterate over the array and 
    - Compare the current element (key) to its predecessor, 
    - If the key element is smaller than its predecessor, 
    - Compare it to the elements before. 
    - Move the greater elements one position up to make space for the swapped element.

'''


# Tc: O(n^2) | Sc: O(1)

def insertionSort(array):
    n = len(array)

   # Traverse and compare with element in front of it
    for i in range(n):
        j = i

        # Check if the predecessor is larger than the current element.
        while j > 0 and array[j-1] > array[j]:
            # Swap
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    
    return array
