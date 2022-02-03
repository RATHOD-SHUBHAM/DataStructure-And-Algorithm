'''

510. Inorder Successor in BST II
Medium

Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Example 1:


Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
Example 2:


Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
 

Follow up: Could you solve it without looking up any of the node's values?





'''




"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
# same for a non BST tree
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            return self.getLeftMostChild(node.right)
        return self.ancestor(node)
    
    def getLeftMostChild(self,node):
        while node.left:
            node = node.left
        return node
    
    def ancestor(self,node):
        while node.parent and node.parent.right == node:
            node = node.parent
            
        return node.parent