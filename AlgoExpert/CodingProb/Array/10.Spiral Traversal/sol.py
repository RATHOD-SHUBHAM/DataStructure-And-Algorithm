# tc: O(m * n) | Sc: (m * n)
def spiralTraverse(array):
    left = 0
    right = len(array[0])

    top = 0
    bottom = len(array)

    op = []

    while top < bottom and left < right:
        # append first row
        for i in range(left, right):
            op.append(array[top][i])

        # move to the next row
        top += 1

        # check if we moved out of matrixx or we have scanned this previously
        if top == bottom:
            break

        # scan last column
        for i in range(top, bottom):
            op.append(array[i][right - 1])

        # move to previous col
        right -= 1

        # check if we have scanned the column already or we moved out of matrix
        if left == right:
            break

        # scan last row
        for i in reversed(range(left, right)):
            op.append(array[bottom - 1][i])


        # decrement the row
        bottom -= 1

        # check if we moved out of matrixx or we have scanned this previously
        if top == bottom:
            break

        # scan the first column
        for i in reversed(range(top, bottom)):
            op.append(array[i][left])

        left += 1

        # check if we have scanned the column already or we moved out of matrix
        if left == right:
            break

    return op
