# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dic = collections.defaultdict()

        op = []

        stack = [[root, 0]]

        min_row = math.inf
        max_row = -math.inf

        while stack:
            node, row = stack.pop()

            dic[row] = node.val
            min_row = min(min_row, row)
            max_row = max(max_row, row)

            if node.left:
                stack.append([node.left, row + 1])
            
            if node.right:
                stack.append([node.right, row + 1])
        
        l_view = []
        for row in range(min_row, max_row + 1):
            l_view.append(dic[row])
        
        return l_view
