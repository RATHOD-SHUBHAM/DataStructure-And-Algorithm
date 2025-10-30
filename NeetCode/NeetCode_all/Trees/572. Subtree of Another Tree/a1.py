# Recursive ----------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot) == True:
                    return True
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return False
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if p and not q:
            return False
        
        if q and not p:
            return False
        
        if p.val != q.val:
            return False
        
        leftTree = self.isSameTree(p.left, q.left)
        print(leftTree)
        rightTree = self.isSameTree(p.right, q.right)
        print(rightTree)

        if leftTree == False or rightTree == False:
            return False
        else:
            return True


# Iterative ----------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot) == True:
                    return True
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return False
    
    def isSameTree(self, p, q):
        queue = [(p , q)]

        while queue:
            p_node, q_node = queue.pop(0)

            if not p_node and not q_node:
                continue
            
            if p_node and not q_node:
                return False
            
            if q_node and not p_node:
                return False
            
            if p_node.val != q_node.val:
                return False
            
            queue.append((p_node.left, q_node.left))
            queue.append((p_node.right, q_node.right))
        
        return True