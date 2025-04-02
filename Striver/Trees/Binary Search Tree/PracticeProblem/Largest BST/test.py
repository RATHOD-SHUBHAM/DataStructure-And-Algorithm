"""
# Top Down Approach:
    1. Check if the current tree(from present root) is a valid BST.
    2. If it is a valid BST, then count the number of nodes in the tree.

"""

# Tc: O(n^2), Sc: O(n)

import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NodeInfo:
    def __init__(self, size, min_val, max_val, isBST):
        self.size = size
        self.min_val = min_val
        self.max_val = max_val
        self.isBST = isBST

class Solution:
    def largestBst(self, root):
        return self.validateBST(root).size

    def validateBST(self, root):
        if not root:
            return NodeInfo(0, math.inf, -math.inf, True)
        
        left = self.validateBST(root.left)
        right = self.validateBST(root.right)
        
        info = NodeInfo(0, 0, 0, False)
        
        info.min_val = min(root.val, left.min_val)
        info.max_val = max(root.val, right.max_val)
        
        if left.isBST and right.isBST and left.max_val < root.val < right.min_val:
            info.isBST = True
            info.size = 1 + left.size + right.size
        else:
            info.isBST = False
            info.size = max(left.size , right.size)
        
        return info
    


# Test cases
def test_cases():
    sol = Solution()
    
    # Test 1: Original case
    root1 = TreeNode(5)
    root1.left = TreeNode(2)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    print("Test 1:", sol.largestBst(root1))  # Should print 3
    
    # Test 2: Complete BST
    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    print("Test 2:", sol.largestBst(root2))  # Should print 5
    
    # Test 3: Single node
    root3 = TreeNode(1)
    print("Test 3:", sol.largestBst(root3))  # Should print 1
    
    # Test 4: Empty tree
    print("Test 4:", sol.largestBst(None))   # Should print 0

    # Test 5: Random case
    root5 = TreeNode(6)
    root5.left = TreeNode(7)
    root5.right = TreeNode(3)
    root5.left.right = TreeNode(2)
    root5.right.left = TreeNode(2)
    root5.right.right = TreeNode(4)
    print("Test 5:", sol.largestBst(root5))   # Should print 3

test_cases()