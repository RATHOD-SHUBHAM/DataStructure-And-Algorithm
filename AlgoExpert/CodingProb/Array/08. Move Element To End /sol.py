# Tc : O(n) | Sc: O(1)

def moveElementToEnd(array, toMove):
    n = len(array)
    
    left = 0
    right = n - 1

    while left < right:
        # move the right pointer until it points to a number which is not toMove
        while left < right and array[right] == toMove:
            right -= 1
        
        # check if left points to toMove and swap it with right
        if array[left] == toMove:
            swap(left, right, array)
            # right -= 1
             
        # move left
        left += 1

    return array

def swap(i , j , array):
    array[i] , array[j] = array[j] , array[i]
