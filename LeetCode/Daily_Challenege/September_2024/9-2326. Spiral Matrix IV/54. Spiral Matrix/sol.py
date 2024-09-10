class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n - 1

        top = 0
        bottom = m - 1

        op = []

        while left <= right and top <= bottom:

            for col in range(left, right + 1):
                op.append(matrix[top][col])
            
            top += 1

            if top > bottom:
                break
            
            for row in range(top , bottom + 1):
                op.append(matrix[row][right])
            
            right -= 1

            if left > right:
                break
            
            for col in reversed(range(left, right + 1)):
                op.append(matrix[bottom][col])
            
            bottom -= 1
            
            for row in reversed(range(top, bottom + 1)):
                op.append(matrix[row][left])

            left += 1
        
        return op