# TC: O(n^2) | Sc: O(1)

def bubbleSort(array):
    n = len(array)

    # Traverse from left to right
    for _ in range(n):
        # compare adj values
        for i in range(n-1):
            if array[i+1] < array[i]:
                # Swapping
                array[i], array[i+1] = array[i+1], array[i]

    return array