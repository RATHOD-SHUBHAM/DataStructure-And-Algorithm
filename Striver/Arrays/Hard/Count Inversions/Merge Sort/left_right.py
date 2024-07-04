def mergeSort(array):

    n = len(array)
    
    if n <= 1:
        return array

    left = 0
    right = n - 1

    mid = left + (right - left)// 2

    '''
        we take mid + 1 because, if this is mid 
        Then consider array of size 2. eg: arr = [2,4]
        then, if left = 0 right = 1 then mid = 0
        Now, if we consider arr[ : mid], then left array will be empty.
    '''
    leftArray = array[ : mid + 1] 
    rightArray = array[mid + 1: ]
    

    leftHalf = mergeSort(leftArray)

    rightHalf = mergeSort(rightArray)


    return merge(leftHalf, rightHalf)

def merge(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))

    i = j = k = 0

    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1

    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1

    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1

    return sortedArray