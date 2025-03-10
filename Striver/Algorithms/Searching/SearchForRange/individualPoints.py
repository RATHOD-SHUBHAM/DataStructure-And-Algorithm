def searchForRange(array, target):
    n = len(array)

    range = [-1, -1]

    left = 0
    right = n - 1

    # Find the left and right point individually
    binarySearch(left, right, range, array, target, goLeft = True)
    binarySearch(left, right, range, array, target, goLeft = False)

    return range

def binarySearch(left, right, range, array, target, goLeft):
    while left <= right:
        mid = left + (right - left) // 2

        val = array[mid]

        if val == target:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    '''
                        Left most found
                    '''
                    range[0] = mid
                    return
                else:
                    right = mid - 1
            else:
                if mid == right or array[mid + 1] != target:
                    '''
                        right  most found
                    '''
                    range[1] = mid
                    return
                else:
                    left = mid + 1
        elif val > target:
            right = mid - 1
        else:
            left = mid + 1
