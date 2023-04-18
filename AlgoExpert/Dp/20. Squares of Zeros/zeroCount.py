# Tc: O(n^3) | Sc: O(n^2)

def squareOfZeroes(matrix):
    n = len(matrix)
    # count the number of zeros to the right and to the bottom
    zeroCount = getCount(matrix)
    print(zeroCount)

    for top in range(n):
        for left in range(n):
            
            windowSize = 2

            while windowSize <= n - top and windowSize <= n - left:
                bottom = top + windowSize - 1
                right = left + windowSize - 1

                if isSquare(top, right, left, bottom, windowSize, zeroCount):
                    return True

                windowSize += 1

    return False

def getCount(matrix):
    n = len(matrix)

    # keeps track of number of zero to the right and no of zero to bottom
    counter_dp_hash = [[None for _ in range(n)] for _ in range(n)]

    # where ever there is zero make the count as 1
    # meaning there is 1 zero at this cell
    for i in range(n):
        for j in range(n):
            # add count
            if matrix[i][j] == 0:
                no_of_zero = 1
            else:
                no_of_zero = 0

            # add the count to the hash
            counter_dp_hash[i][j] = {
                "no_of_zero_below" : no_of_zero,
                "no_of_zero_to_right" : no_of_zero
            }

    # no count for each cell how many zero is there below it and to the right of it
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if matrix[i][j] == 1:
                continue

            if i < n - 1:
                counter_dp_hash[i][j]["no_of_zero_below"] += counter_dp_hash[i + 1][j]["no_of_zero_below"]
            
            if j < n - 1:
                counter_dp_hash[i][j]["no_of_zero_to_right"] += counter_dp_hash[i][j + 1]["no_of_zero_to_right"]

    return counter_dp_hash

def isSquare(top, right, left, bottom, windowSize, zeroCount):
    # check if there are enough zero to fill in the window size
    border_top_to_bottom = zeroCount[top][left]["no_of_zero_below"] >= windowSize
    border_top_to_right= zeroCount[top][left]["no_of_zero_to_right"] >= windowSize

    border_right_to_bottom = zeroCount[top][right]["no_of_zero_below"] >= windowSize

    border_bottom_to_right = zeroCount[bottom][left]["no_of_zero_to_right"] >= windowSize

    return border_top_to_bottom and border_top_to_right and border_right_to_bottom and border_bottom_to_right
