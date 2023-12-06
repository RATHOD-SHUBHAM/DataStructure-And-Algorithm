'''
In Bubble Sort algorithm, 

    - Traverse from left and compare adjacent elements and the higher one is placed at right side. 
    - In this way, the largest element is moved to the rightmost end at first. 
    - This process is then continued to find the second largest and place it and so on until the data is sorted.


'''


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
                
