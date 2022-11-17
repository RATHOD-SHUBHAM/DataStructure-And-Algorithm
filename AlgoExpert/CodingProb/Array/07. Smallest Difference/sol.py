# tc: O(nlog(n) + mlog(m)) | Sc: O(1)

import math
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort() # nlog(n)
    arrayTwo.sort() # mlog(m)
    n_one = len(arrayOne)
    n_two = len(arrayTwo)

    min_difference = math.inf # keep track of cur min difference

    idxOne = idxTwo = 0

    while idxOne < n_one and idxTwo < n_two:
        numOne = arrayOne[idxOne]
        numTwo = arrayTwo[idxTwo]

        # get the difference between numbers
        difference = abs(numOne - numTwo)

        # if the difference becomes 0, this is the minimum difference
        if difference == 0:
            return [numOne , numTwo]

        # check if the current difference is smaller than the minimum difference
        if difference < min_difference:
            min_difference = difference
            min_diff = [numOne , numTwo]

        # further more reduce the difference between numbers
        if numOne < numTwo:
            idxOne += 1
        elif numTwo < numOne:
            idxTwo += 1

    return min_diff
    
    