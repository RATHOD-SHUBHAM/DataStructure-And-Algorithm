"""
# Bottom up approach

Check if current tree is a valid BST:
    Inorder to do so, we compare the root value with:
        i. Maximum value in left subtree: Right most node in left subtree
        ii. Minimum value in right subtree: Left most node in right subtree
    If the root value is greater than maximum value in left subtree and less than minimum value in right subtree, then the current tree is a valid BST.

Track:
min: Track the minimum value in the tree
max: Track the maximum value in the tree

So from the rigth subtree we check the min value and from the left subtree we check the max value.
"""

import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NodeInfo:
    def __init__(self, size, min_val, max_val, is_bst):
        self.size = size          # Size of largest BST
        self.min = min_val        # Minimum value in tree
        self.max = max_val        # Maximum value in tree
        self.is_bst = is_bst      # If current subtree is BST

class Solution:
    def largestBst(self, root):
        def solve(root):
            if not root:
                return NodeInfo(0, math.inf, -math.inf, True)
            
            # Get left and right subtree information
            left = solve(root.left)
            right = solve(root.right)
            
            # Current node's info
            info = NodeInfo(0, 0, 0, False)
            
            # Update min and max values for current subtree
            info.min = min(root.val, left.min)
            info.max = max(root.val, right.max)
            
            # Check if current subtree is BST
            if (left.is_bst and right.is_bst and
                left.max < root.val < right.min):
                info.is_bst = True
                info.size = left.size + right.size + 1
            else:
                info.is_bst = False
                info.size = max(left.size, right.size)
            
            return info
        
        return solve(root).size

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