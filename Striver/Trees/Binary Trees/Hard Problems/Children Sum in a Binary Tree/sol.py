'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        return self.postorder(root)
    
    def postorder(self, node):
        if not node:
            return 1
        
        # leftchild
        leftchild_sum = self.postorder(node.left)
        
        # rightChild
        rightchild_sum = self.postorder(node.right)
        
        cur_node_sum = 0
        # Handle leaf nodes
        if not node.left and not node.right:
            cur_node_sum = 1
        else:
            left_child_val = node.left.data if node.left else 0
            right_child_val = node.right.data if node.right else 0
            
            if node.data == left_child_val + right_child_val:
                cur_node_sum = 1
            else:
                cur_node_sum = 0
        
        return cur_node_sum and leftchild_sum and rightchild_sum