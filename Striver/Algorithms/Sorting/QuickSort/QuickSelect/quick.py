'''
    Kth largest or Kth smallest
        can be found with Quick Select
'''

# Tc: O(n^2) | Sc: O(1)
def quickselect(array, k):
    n = len(array)

    start = 0
    end = n - 1

    k = k - 1

    return quick(start, end, k, array)


def quick(start, end, k, array):
    # Quick Sort Part
    if start > end:
        return

    # Pointers
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(left, right, array)

        if array[left] <= array[pivot]:
            left += 1

        if array[right] >= array[pivot]:
            right -= 1

    swap(pivot, right, array)

    # Quick Select
    if right == k:
        return array[right]
    elif right > k:
        end = right - 1
        return quick(start, end, k, array)
    else:
        start = right + 1
        return quick(start, end, k, array)
        


def swap(i , j , array):
    array[i], array[j] = array[j], array[i]