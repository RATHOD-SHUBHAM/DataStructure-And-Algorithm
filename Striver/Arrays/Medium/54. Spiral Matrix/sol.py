class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])

        top = 0
        bottom = len(matrix)

        op = []

        while top < bottom and left < right:
            # top - left to right
            for i in range(left, right):
                op.append(matrix[top][i])
            
            top += 1

            if top == bottom:
                break
            
            # right - top to bottom
            for i in range(top, bottom):
                op.append(matrix[i][right - 1])

            right -= 1

            if right == left:
                break
            
            # bottom - right to left
            for i in reversed(range(left, right)):
                op.append(matrix[bottom - 1][i])
            
            bottom -= 1

            if top == bottom:
                break
            
            # left - bottom to top
            for i in reversed(range(top, bottom)):
                op.append(matrix[i][left])
            
            left += 1

            if left == right:
                break
        
        return op