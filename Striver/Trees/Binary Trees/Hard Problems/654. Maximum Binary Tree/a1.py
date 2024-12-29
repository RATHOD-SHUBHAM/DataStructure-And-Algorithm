# ----------- Recursive Solution -----------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_val = max(nums)
        idx = nums.index(max_val)
        
        # Create a root node
        root = TreeNode(max_val)

        # Get the left child
        nums_left_half = nums[ : idx]
        root.left = self.constructMaximumBinaryTree(nums_left_half)

        # Get the right child
        nums_right_half = nums[idx+1 : ]
        root.right = self.constructMaximumBinaryTree(nums_right_half)

        return root

# ----------- Iterative Solution -----------

# Tc and Sc: O(n).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        stack_of_nodes = []

        for num in nums:
            node = TreeNode(num)

            # Set the smaller nodes as the left child
            while stack_of_nodes and stack_of_nodes[-1].val < num:
                node.left = stack_of_nodes.pop()
            
            # Set the current node as the right child
            if stack_of_nodes:
                # stack_of_nodes[-1] will be the max number
                stack_of_nodes[-1].right = node
            
            stack_of_nodes.append(node)
        
        # The root of the tree is the first node added to the stack
        return stack_of_nodes[0]