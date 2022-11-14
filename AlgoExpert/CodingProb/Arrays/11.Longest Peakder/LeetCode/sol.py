'''

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]



'''


# TIme = O(m * n)
# space = O(1) : if we dont consider op

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # initialize left right top and bottom pointer
        left = top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        
        res = []
        
        while left < right and top < bottom:
            # move from left to right: top row
            for i in range(left , right):
                res.append(matrix[top][i])
            # print("res: ",res)
            top += 1
            
            # If there is only one row: my pointers would have touched each other
            if top == bottom:
                break

            # move from top to bottom on right col
            for i in range(top , bottom):
                res.append(matrix[i][right-1])
            # print("res: ",res)
            right -= 1

            # If there is only one col: my pointers would have touched each other
            if left == right:
                break

            # move from right to left
            for i in reversed(range(left, right)):
                res.append(matrix[bottom - 1][i])
            # print("res: ",res)
            bottom -= 1

            # move from bottom to top on left col
            for i in reversed(range(top, bottom)):
                res.append(matrix[i][left])
            # print("res: ",res)
            left += 1
        
            # print("\n")
        return res
        
        