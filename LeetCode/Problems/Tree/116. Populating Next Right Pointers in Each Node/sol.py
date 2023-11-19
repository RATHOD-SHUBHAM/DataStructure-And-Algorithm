"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        parentNode = None
        isLeftChild = None
        self.dfs(root, parentNode, isLeftChild)
        return root
    
    def dfs(self, root, parentNode, isLeftChild):
        if not root:
            return
        
        self.dfs(root.left, root, True)
        
        rightChild = root.right
        
        if parentNode is None:
            root.next = None
        
        elif isLeftChild == True:
            root.next = parentNode.right
        
        elif isLeftChild == False:
            if parentNode.next is None:
                root.next = None
            else:
                root.next = parentNode.next.left
                
        self.dfs(rightChild, root, False)
        
        return
            