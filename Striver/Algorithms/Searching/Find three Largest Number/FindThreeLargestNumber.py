# Tc: O(n) | Sc: O(1)

def findThreeLargestNumbers(array):
    res = [None, None, None]
    compare(res, array)
    return res

def compare(res, array):
    '''
        Comapre the number with 3 values
    '''
    for num in array:
        if res[2] == None or num > res[2]:
            shift(2, num, res)
        elif res[1] == None or num > res[1]:
            shift(1, num, res)
        elif res[0] == None or num > res[0]:
            shift(0, num, res)

    return

def shift(idx, num, res):
    if res[idx] == None:
        # First encounter
        res[idx] = num
    else:
        # Shift and place value in correct position
        for i in range(0, idx + 1):
            if i == idx:
                res[idx] = num
            else:
                # shift left
                res[i] = res[i+1]
    return