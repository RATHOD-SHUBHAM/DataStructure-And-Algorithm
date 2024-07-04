def mergeSort(array):

    n = len(array)
    
    if n <= 1:
        return array
    
    mid = n // 2

    leftArray = array[ : mid ] 
    rightArray = array[mid : ]
    

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