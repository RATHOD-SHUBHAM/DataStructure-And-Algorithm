# Tc: O(n^2) | Sc: O(1)
def selectionSort(array):
    n = len(array)

    for i in range(n):
        #select a min value
        min_val = array[i]

        # iterate over and bring the actual min value
        for j in range(i , n):
            if array[j] < min_val:
                # make the current value min
                min_val = array[j]
                # swap the value
                swap(array, i, j)

    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]