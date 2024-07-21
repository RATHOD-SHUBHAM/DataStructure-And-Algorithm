'''
    Time Complexity = O(n+m)
    Space complexity = O(1)

    Start from last column and move diagonally downwards, this way we eliminate searching in zone which are smaller than the desired value
'''

def searchInSortedMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0]) - 1
    
    row = 0
    col = n

    while row < m and col >= 0:
        cur_val = matrix[row][col]

        if cur_val == target:
            return [row, col]
        elif cur_val > target:
            col -= 1
        else:
            row += 1

    return [-1, -1]