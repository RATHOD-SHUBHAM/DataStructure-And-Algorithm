def quickselect(array, k):
    pos = k - 1 # index 0
    return helper(0 , len(array) - 1 , array , pos)

def helper(startIdx, endIdx , array , pos):
    while True:
        if startIdx > endIdx:
            break
    
        pivot = startIdx
        left = startIdx + 1
        right = endIdx
    
        while left <= right:
            if array[pivot] < array[left] and array[right] < array[pivot]:
                swap(left , right , array)
    
            if array[left] <= array[pivot]:
                left += 1
    
            if array[pivot] <= array[right]:
                right -= 1
    
        swap(pivot , right , array)
    
        if right == pos:
            return array[right]
            
        elif right > pos:
            endIdx = right - 1
            
        else:
            startIdx = right + 1

def swap(i , j , array):
    array[i] , array[j] = array[j] , array[i]
