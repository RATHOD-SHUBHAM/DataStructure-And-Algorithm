# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        cur_node = head

        while top <= bottom and left <= right:
            # Left to Right
            for col in range(left, right + 1):
                if cur_node is None:
                    break
                
                matrix[top][col] = cur_node.val
                cur_node = cur_node.next
            
            top += 1

            if top > bottom:
                break
            
            # Top to Bottom
            for row in range(top, bottom + 1):
                if cur_node is None:
                    break
                
                matrix[row][right] = cur_node.val
                cur_node = cur_node.next
            
            right -= 1

            if left > right:
                break
            
            # Right to Left
            for col in reversed(range(left, right + 1)):
                if cur_node is None:
                    break
                
                matrix[bottom][col] = cur_node.val
                cur_node = cur_node.next
            
            bottom -= 1

            # Bottom to Top
            for row in reversed(range(top, bottom + 1)):
                if cur_node is None:
                    break
                
                matrix[row][left] = cur_node.val
                cur_node = cur_node.next
            
            left += 1
        
        # print(matrix)

        return matrix

