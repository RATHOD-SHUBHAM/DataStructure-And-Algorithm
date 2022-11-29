def zigzagTraverse(array):
    dic = {}

    # get the value at each sum of indices
    # index = row + col
    # eg: value at index 0, index 1  index 2 and so on
    for row in range(len(array)):
        for col in range(len(array[0])):
            if row+col not in dic:
                dic[row+col] = [array[row][col]]
            else:
                dic[row+col].append(array[row][col])


    res = []

    for key, value in dic.items():
        #all the items at index 1,3,5,7... are reversed
        if key % 2 == 0:
            [res.append(x) for x in value] 
        else:
            [res.append(x) for x in reversed(value)] # reverse entry

    return res
