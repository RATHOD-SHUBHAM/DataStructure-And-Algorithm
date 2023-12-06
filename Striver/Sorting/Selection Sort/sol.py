'''
Selection sort works by taking the smallest element in an unsorted array and bringing it to the front. 
You’ll go through each item (from left to right) until you find the smallest one. 
The first item in the array is now sorted, while the rest of the array is unsorted.



'''

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
                
                
                
