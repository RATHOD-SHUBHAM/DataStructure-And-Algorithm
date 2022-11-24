# Using Dictionary flagset
# flag the already visited number
# Tc and Sc = O(n)

import math
def largestRange(array):
    longestRange = -math.inf
    op = [-1, -1]
    dic = {}

    # setting the flag value
    for num in array:
        dic[num] = True

    for num in array:
        # check if the number has been already visited
        if dic[num] == False:
            continue

        cur_range = 1
        start_range = num - 1
        end_range = num + 1

        # getting the smallest number
        while start_range in  dic:
            cur_range += 1
            start_range -= 1

        # getting the largest number
        while end_range in dic:
            cur_range += 1
            end_range += 1

        if cur_range > longestRange:
            longestRange = cur_range
            op[0] = start_range + 1 # start_range will be pointing at number that is not available
            op[1] = end_range - 1 # start_range will be pointing at number that is not available


    return op
            

        

    
