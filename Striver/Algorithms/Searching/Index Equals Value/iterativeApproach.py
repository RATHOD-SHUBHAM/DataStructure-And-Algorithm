'''
Since the value is sorted:
	1. if the value is less than index --> all elements on the left will not have index that match the value
	2. if the value is greater than index --> all the elements on the right will nont have index that will match the value

'''


# time complexity = O(log(n))
# Space complexity = O(1)


def indexEqualsValue(array):
    n = len(array)

    left = 0
    right = n - 1

    while left <= right:

        mid = left + (right - left) // 2
    
        # index = value
        if mid == array[mid]:
            # check if this is the minimum index
            if (mid == 0) or (array[mid - 1] != mid - 1):
                return mid
            else:
                # if not move left
                right = mid - 1
    
        elif mid > array[mid]:
            left = mid + 1
        elif mid < array[mid]:
            right = mid - 1

    return -1
	
