'''
In Bubble Sort algorithm, 

    - Traverse from left and compare adjacent elements and the higher one is placed at right side. 
    - In this way, the largest element is moved to the rightmost end at first. 
    - This process is then continued to find the second largest and place it and so on until the data is sorted.

Psudo Code:
    - Compare for n time
        - Try placing the current largest element in its correct place (right most).
            - swap with the adjacent element if condition match

'''


# Tc: O(n^2) | Sc: O(1)

def bubbleSort(array):
    n = len(array)

    # Do the comparison for n times
    for _ in range(n):
        # For each time: Place the current Larger element in right place
        for i in range(n-1):
            if array[i] > array[i + 1]:
                # Swap
                array[i], array[i+1] = array[i+1], array[i]


    return array
                
