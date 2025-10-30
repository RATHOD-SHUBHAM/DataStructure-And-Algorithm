def mergeSort(array):
    n = len(array)

    if n == 1:
        return array

    left = 0
    right = n - 1

    mid = left + (right - left) // 2


    left_side_array = array[ : mid + 1]
    # print(left_side_array)
    right_side_array = array[mid + 1: ]
    # print(right_side_array)

    left_array = mergeSort(left_side_array)
    right_array = mergeSort(right_side_array)

    return mergeSort_array(left_array , right_array)


def mergeSort_array(left_array , right_array):
    len_left = len(left_array)
    len_right = len(right_array)

    sorted_array = [None] * (len_left + len_right)

    i = j = k = 0

    while i < len_left and j < len_right:
        if left_array[i] < right_array[j]:
            sorted_array[k] = left_array[i]
            i += 1
        else:
            sorted_array[k] = right_array[j]
            j += 1
         
        k += 1

    # remaining element
    while i < len_left:
        sorted_array[k] = left_array[i]
        i += 1
        k += 1

    while j < len_right:
        sorted_array[k] = right_array[j]
        j += 1
        k += 1

    return sorted_array