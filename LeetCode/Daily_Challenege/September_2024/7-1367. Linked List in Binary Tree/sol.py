# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        cur_ll_node = head
        node = root

        return self.preOrderTraversal(node, cur_ll_node)
    
    def preOrderTraversal(self, node, cur_ll_node):
        if not node:
            return False

        if self.validatePath(node, cur_ll_node):
            # Found a valid path from here
            return True
        
        leftPath = self.preOrderTraversal(node.left, cur_ll_node)
        rightPath = self.preOrderTraversal(node.right, cur_ll_node)

        # If one of the path is true, then we found the subpath
        return leftPath or rightPath
    

    def validatePath(self, node, cur_ll_node):
        if cur_ll_node is None:
            return True # we have found our path
        
        if node is None:
            return False # we reached the end of Tree

        if node.val != cur_ll_node.val:
            return False # value doesnot match - Move down the tree
        
        # if the value match, further move down in the sub-tree
        leftSubTree = self.validatePath(node.left, cur_ll_node.next)
        rightSubTree = self.validatePath(node.right, cur_ll_node.next)

        return leftSubTree or rightSubTree
    


