class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top = left = 0
        right = n - 1
        bottom = m - 1

        op = []

        while top <= bottom and left <= right:
            # 1] top: move from left to right
            for i in range(left, right + 1):
                op.append(matrix[top][i])

            top += 1
            
            if bottom < top:
                break
            
            
            # 2] right: move from top to bottom
            for i in range(top, bottom + 1):
                op.append(matrix[i][right])
            
            right -= 1

            if right < left:
                break

            
            # 3] bottom: move from right to left
            for i in reversed(range(left, right + 1)):
                op.append(matrix[bottom][i])
            
            bottom -= 1

            # if bottom < top:
            #     break

            
            # 4] left: move from bottom to top
            for i in reversed(range(top, bottom + 1)):
                op.append(matrix[i][left])
            
            left += 1

            # if right < left:
            #     break
        
        return op
