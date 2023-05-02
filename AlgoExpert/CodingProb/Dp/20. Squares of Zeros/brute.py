# Tc: O(n^4) | Sc: O(1)
def squareOfZeroes(matrix):
    n = len(matrix)

    # start from one corner and expand the window size to the fullest and then move forward.
    # because if we go window by window getting back to same corner will be difficult
    for top in range(n):
        for left in range(n):

            windowSize = 2

            while windowSize <= n - top and windowSize <= n - left:
                right = left + windowSize - 1
                bottom = top + windowSize - 1

                if isSquare(top, left, right, bottom, matrix):
                    return True


                windowSize += 1

    return False

def isSquare(top, left, right, bottom, matrix):

    # move across the borders and check if they 0 or not
    
    for row in range(top , bottom + 1):
        if matrix[row][left] != 0 or matrix[row][right] != 0:
            return False

    for col in range(left , right + 1):
        if matrix[top][col] != 0 or matrix[bottom][col] != 0:
            return False

    return True
