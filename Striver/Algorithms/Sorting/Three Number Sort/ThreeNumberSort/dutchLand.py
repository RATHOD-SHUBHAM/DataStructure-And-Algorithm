# Tc: O(n) | Sc: O(1)

# DutchLand Sorting Problem
def threeNumberSort(array, order):
    first_ele = order[0]
    last_ele = order[2]

    n = len(array)

    left = 0 # keep track of first/left element
    p = 0
    right = n - 1 # keep track of last/right element

    while p <= right:
        if array[p] == first_ele:
            '''
                Placing the first element to the left
            '''
            swap(left, p , array)
            left += 1
            p += 1
        elif array[p] == last_ele:
            '''
                Placing the last element to the right
            '''
            swap(right, p, array)
            right -= 1
        else:
            p += 1

    return array

def swap(x , y, array):
    array[x], array[y] = array[y], array[x]