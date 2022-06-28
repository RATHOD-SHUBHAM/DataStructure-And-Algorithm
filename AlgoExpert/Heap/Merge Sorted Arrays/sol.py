def mergeSortedArrays(arrays):
    if len(arrays) <= 1:
        return arrays

    while len(arrays) > 1:
        mergedArray = []

        for i in range(0 , len(arrays) , 2):
            array_one = arrays[i]
            # print(array_one)
            array_two = arrays[i+1] if (i + 1) < len(arrays) else None
            # print(array_two)

            mergedArray.append(mergeSort(array_one, array_two))
            # print(mergedArray)
            # print("\n")

        arrays = mergedArray
    # print("arrays: ",arrays[0])

    return arrays[0]

def mergeSort(array_one , array_two):
    # pointers
    p1 = 0
    p2 = 0
    op = []

    if array_one is None:
        return array_two
    if array_two is None:
        return array_one

    while p1 < len(array_one) and p2 < len(array_two):
        
        if array_one[p1] < array_two[p2]:
            op.append(array_one[p1])
            p1 += 1
        else:
            op.append(array_two[p2])
            p2 += 1

    # one of the pointer will be out
    if p1 < len(array_one):
        op += array_one[p1 : ]

    if p2 < len(array_two):
        op += array_two[p2 : ]

    return op
            
            
