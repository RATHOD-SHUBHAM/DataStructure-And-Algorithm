# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rowBegin, colBegin = 0, 0
        rowEnd = len(matrix)
        colEnd = len(matrix[0])
        result = []

        while rowBegin < rowEnd and colBegin < colEnd:
            for i in range(colBegin, colEnd):
                result.append(matrix[rowBegin][i])  # 1234
            for j in range(rowBegin + 1, rowEnd - 1):
                result.append(matrix[j][colEnd - 1])  # 12348

            if rowBegin + 1 != rowEnd:
                for i in range(colEnd - 1, colBegin - 1, -1):
                    result.append(matrix[rowEnd - 1][i])  # 12348,12,11,10,9

            if colBegin + 1 != colEnd:
                for j in range(rowEnd - 2, rowBegin, -1):
                    result.append(matrix[j][colBegin])

            rowBegin += 1
            colBegin += 1
            rowEnd -= 1
            colEnd -= 1
        return result