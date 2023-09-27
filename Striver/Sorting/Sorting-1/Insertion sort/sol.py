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
