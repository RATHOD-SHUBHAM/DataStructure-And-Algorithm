# ---------------- Insert Node into BST ----------------
# Brute Force: Insert Node into BST.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        # Create root node
        root = TreeNode(preorder[0])

        # Insert into BST
        for i in range(1, n):
            val = preorder[i]
            self.insertNode(root, val)
        
        return root
    
    def insertNode(self, root, val):
        if val < root.val:
            if root.left:
                self.insertNode(root.left, val)
            else:
                root.left = TreeNode(val)
        elif val > root.val:
            if root.right:
                self.insertNode(root.right, val)
            else:
                root.right = TreeNode(val)

# ---------------- Inoder Preorder Construction ----------------

# Inorder Preorder Construction

# Tc: O(nlogn) + O(n) | Sc: O(1)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.preorder_idx = 0
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        inorder = sorted(preorder)

        inorder_dict = {val : idx for idx, val in enumerate(inorder)}

        start = 0
        end = n - 1

        return self.construct(start, end, preorder, inorder_dict)
    
    def construct(self, start, end, preorder, inorder_dict):
        if start > end:
            return
        
        root_val = preorder[self.preorder_idx]
        self.preorder_idx += 1

        root = TreeNode(root_val)

        root_idx = inorder_dict[root_val]

        root.left = self.construct(start, root_idx - 1, preorder, inorder_dict)
        root.right = self.construct(root_idx + 1, end, preorder, inorder_dict)

        return root


# ---------------- Range ----------------

# Valid BST.

# Tc: O(N) | Sc: O(N)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.idx = 0

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        minRange = -math.inf
        maxRange = math.inf
        return self.validBST(minRange, maxRange, preorder, n)
    
    def validBST(self, minRange, maxRange, preorder, n):
        if self.idx == n:
            return None
        
        node_val = preorder[self.idx]

        # Validate
        if node_val <= minRange or node_val >= maxRange:
            return None

        # Create node
        self.idx += 1
        root = TreeNode(node_val)

        root.left = self.validBST(minRange, node_val, preorder, n)
        root.right = self.validBST(node_val, maxRange, preorder, n)

        return root


# ---------------- Stack ----------------

# Tc and Sc: O(n)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        root_val = preorder[0]
        root = TreeNode(root_val)

        stack = [root]

        for i in range(1, n):
            child_val = preorder[i]

            node = stack[-1]
            child = TreeNode(child_val)

            while stack and stack[-1].val < child.val:
                # Remove all the node that are smaller to the child node
                node = stack.pop()
                
            
            if node.val < child.val:
                # add the right child
                node.right = child
            elif node.val > child.val:
                # add the left child
                node.left = child
            
            stack.append(child)
        
        return root