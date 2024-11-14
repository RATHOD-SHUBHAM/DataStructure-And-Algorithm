# Tc and Sc: O(n + m) 
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    n1 = len(arrayOne)
    n2 = len(arrayTwo)

    sortedArray = []

    p = q = 0

    while p < n1 and q < n2:
        if arrayOne[p] < arrayTwo[q]:
            sortedArray.append(arrayOne[p])
            p += 1
        else:
            sortedArray.append(arrayTwo[q])
            q += 1

    sortedArray += arrayOne[p : ] + arrayTwo[q : ]


    n = len(sortedArray)
    mid = n // 2

    if n % 2 == 0:
        
        median = (sortedArray[mid] + sortedArray[mid-1]) / 2
        return median
    else:
        return sortedArray[mid]