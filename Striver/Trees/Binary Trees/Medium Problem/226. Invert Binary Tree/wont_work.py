'''
First this is really complex to solve like this

Second since this is not a perfect binary tree , we will not be able to store null values.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    
    def grab_nodes(self, root):
        queue = [root]

        while queue:
            q_len = len(queue)
            cur_nodes = []

            for _ in range(q_len):
                node = queue.pop(0)

                cur_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            self.nodes += cur_nodes[::-1]
        
        return
    

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        self.grab_nodes(root)
        print(self.nodes)

        # Build Tree
        new_root = self.buildTree()

        return new_root
    
    def buildTree(self):
        root_val = self.nodes[0]
        root = TreeNode(root_val)

        n = len(self.nodes)

        parent_idx = ((n-1) - 1) // 2

        treenodes = [root]

        idx = 0

        for i in range(parent_idx + 1):
            cur_node = treenodes[idx]

            left_child_idx = 2 * idx + 1
            if left_child_idx < n:
                left_child = TreeNode(self.nodes[left_child_idx])
                cur_node.left = left_child
                treenodes.append(left_child)  # Add left child to the node list

            # Right child index
            right_child_idx = 2 * idx + 2
            if right_child_idx < n:  # If within bounds
                right_child = TreeNode(self.nodes[right_child_idx])
                cur_node.right = right_child
                treenodes.append(right_child)  # Add right child to the node list
            
            # Move to the next parent node (in the tree_nodes list)
            idx += 1
        
        return root
        