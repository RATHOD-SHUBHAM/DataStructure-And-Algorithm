# Time Complexity = O(n) , where n is the length of array.
# spacea complexity = O(1)

def searchForRange(array, target):
    l = 0 
    r = len(array) - 1

    while l < r:
        if array[l] != target:
            l += 1
        if array[r]!= target:
            r -= 1
        if array[l] == target and array[r] == target:
            return ([l,r])
        
    return ([-1,-1])
