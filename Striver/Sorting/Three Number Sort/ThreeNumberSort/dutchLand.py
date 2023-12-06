# Tc: O(n) | Sc: O(1)

# DutchLand Problem
def threeNumberSort(array, order):
    
    first_ele = order[0]
    last_ele = order[-1]

    n = len(array)
    
    # Pointers
    p0 = 0
    left = 0
    right = n - 1

    while left <= right:
        
        if array[left] == last_ele:
            
            array[left] , array[right] = array[right] , array[left]
            right -= 1
        
        elif array[left] == first_ele:

            array[left] , array[p0] = array[p0], array[left]
            left += 1
            p0 += 1

        else:
            left += 1


    return array