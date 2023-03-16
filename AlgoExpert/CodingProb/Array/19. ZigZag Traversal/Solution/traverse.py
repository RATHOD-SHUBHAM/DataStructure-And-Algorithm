# TC and Sc: O(n)

def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    row = col = 0

    goingDown = True

    res = []

    while isBound(row, col, height, width):
        # append the value first
        res.append(array[row][col])

        # move in the direction that was assigned
        if goingDown == True:
            # check if we are at the border to change direction
            # at the border I cant diagonally move down or move down
            if col == 0 or row == height:
                goingDown = False # next number should move up

                # only in the final row of col 0 we will move right else we will keep going down
                if row == height: 
                    # move right
                    col += 1
                else:
                    # move down
                    row += 1
            else:
                # move diagonally down
                row += 1
                col -= 1

        else:
            # check if we are at the border to change direction
            # at the border I cant diagonally move up or move up
            if row == 0 or col == width:
                # next number should move down as i cant move up
                goingDown = True

                # only in the final col of row 0 we will move down else we will keep going left
                if col == width:
                    # move down
                    row += 1
                else:
                    # move left
                    col += 1
            else:
                # move diagonally up
                row -= 1
                col += 1

    return res
                    
def isBound(row, col, height, width):
    return row >= 0 and col >= 0 and row <= height and col <= width