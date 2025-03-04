# Tc and Sc: O(n) | O(h)


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.node_count = 0
        self.count = 0
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            self.count += 1
            self.node_count = max(self.node_count, self.count)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return self.node_count
    
# ----------- Width of the tree ----------------

# Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_nodes = 0
        queue = [[root, 0]]

        while queue:
            q_len = len(queue)
            left_pos = queue[0][1]

            for _ in range(q_len):
                node, pos = queue.pop(0)

                new_pos = pos - left_pos

                if node.left:
                    left_child_pos = 2 * new_pos + 1
                    queue.append([node.left, left_child_pos])
                
                if node.right:
                    right_child_pos = 2 * new_pos + 2
                    queue.append([node.right, right_child_pos])
            
            cur_width = pos - left_pos + 1

            total_nodes += cur_width
        
        return total_nodes
    

# ----------- Height of the tree ----------------

# Tc: O(logN) | Sc: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.no_of_nodes(root)
    
    def no_of_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Check if the tree is balanced or not
        leftChild_height = self.height_of_lefttree(root)
        rightChild_height = self.height_of_righttree(root)

        if leftChild_height == rightChild_height:
            """The Tree is Balanced"""
            return (2 ** rightChild_height) - 1 # (2^h) - 1
        else:
            """The Tree is Not Balanced"""
            leftChild_nodes = self.no_of_nodes(root.left)
            rightChild_nodes = self.no_of_nodes(root.right)
        
        return 1 + leftChild_nodes + rightChild_nodes
    
    def height_of_lefttree(self, root: Optional[TreeNode]) -> int:
        height=0
        while root:
            height += 1
            root = root.left
        
        return height
    
    def height_of_righttree(self, root: Optional[TreeNode]) -> int:
        height=0
        while root:
            height += 1
            root = root.right
        
        return height
        
    