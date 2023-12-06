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
        
        min_val = array[i]

        for j in range(i, n):

            cur_val = array[j]
            
            # If the current val < min_val, push it in front of current val
            if min_val > cur_val:

                min_val = cur_val
                
                array[i] , array[j] = array[j] , array[i]

    return array
                
                
                

