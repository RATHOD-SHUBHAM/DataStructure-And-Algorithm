# No of inversion = How unsorted the array is 
def countInversions(array):
    n = len(array)

    left = 0
    right = n - 1

    return mergeSort(left, right , array)

def mergeSort(left, right, array):
    if right - left < 1:
        return 0

    mid = left + (right - left) // 2

    leftArray = mergeSort(left, mid, array)
    rightArray = mergeSort(mid + 1, right, array)

    inversion = merge(left, mid + 1, right, array)


    return leftArray + rightArray + inversion

def merge(left, start, right, array):

    '''
        Start: Start position of right array
        right : End Index
    '''
    sorted_array = []
    i = left
    j = start

    count_inversion = 0

    while i < start and j < right + 1:
        if array[i] <= array[j]:
            sorted_array.append(array[i])
            i += 1
        else:
            '''
                i > j : So increase the count
            '''
            count_inversion += start - i
            
            sorted_array.append(array[j])
            j += 1

    sorted_array += array[i : start] + array[j : right  + 1]

    for i in range(len(sorted_array)):
        array[i + left] = sorted_array[i]

    return count_inversion
        
    
        
    
