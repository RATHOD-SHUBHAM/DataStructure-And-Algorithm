# Tc and Sc: O(mn)
def minimumPassesOfMatrix(matrix):
    no_of_passes = countPasses(matrix)
    # givens the min_no_passes to convert the negative numbers beside the positive numbers
    print("no_of_passes : ", no_of_passes)
    
    anyNegative = checkNegative(matrix)

    # check if there are neative number still remaining
    if anyNegative:
        return -1
    else:
        # -1 : because we count the initial positive number as well, so exclude that
        return no_of_passes - 1


def countPasses(matrix):
    # get all the positive numbers
    queue = getPositive(matrix)
    # print("queue: ", queue)

    passes = 0
    
    # while there are element in queue
    while queue:
        # initial len will help us loop only for specific count ie initial count
        queue_len = len(queue)
        print("queue: ", queue)

        while queue_len > 0:
            row , col = queue.pop(0) # pop the positive number
                
            # explore the neighbor
            adj_nei = getAdjacentNeighbor(row, col, matrix)

            for nei in adj_nei:
                nei_row, nei_col = nei

                # if the neighbor is negative convert to positive
                if matrix[nei_row][nei_col] < 0:
                    matrix[nei_row][nei_col] *= -1
                    queue.append([nei_row, nei_col])
                    
                # if neigbor is zero then we cant change anything
                # if the neigbor is positive then they have been previously explored
                elif matrix[nei_row][nei_col] >= 0:
                    continue

            # since the node is explored - reduce the count
            queue_len -= 1

        # once the queue len becomes 0, ie will be one pass , where all the negative number are converted to positive
        passes += 1

    return passes



def getPositive(matrix):
    positive_number_idx = []

    row_len = len(matrix)
    col_len = len(matrix[0])

    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] > 0:
                positive_number_idx.append([row, col])

    return positive_number_idx


def getAdjacentNeighbor(row, col, matrix):
    adjNeighbor = []

    # up
    if row > 0:
        adjNeighbor.append([row - 1 , col])
    # down
    if row < len(matrix) - 1:
        adjNeighbor.append([row + 1 , col])

    # left
    if col > 0:
        adjNeighbor.append([row , col - 1])
    # right
    if col < len(matrix[0]) - 1:
        adjNeighbor.append([row , col + 1])

    return adjNeighbor

def checkNegative(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])

    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] < 0:
                return True

    return False