"""
Idea seems to be right but the solution wont work.

Here's why:

We have to modify the root node of the tree in place.
That means we cant create a special linked list from the values of the tree node.

We have to modify the tree itself.

How do we know that?
def flatten(self, root: Optional[TreeNode]) -> None:

If we observer the function signature, we see that the return type is None.
That means we return nothing. We have to modify the tree in place.

"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class ListNode:
    def __init__(self, val=-math.inf, next = None):
        self.val = val
        self.next = None

class Solution:
    def getback(self, node):
        nums = []

        while node is not None:
            nums.append(node.val)
            node = node.next
        return nums

    def build_linkedlist(self, nums):
        dummy = prevNode = ListNode(-math.inf)

        while nums:
            cur_val = nums.pop(0)

            curNode = ListNode(cur_val)
            prevNode.next = curNode
            prevNode = curNode
            
        
        return dummy.next


    def preorderTraversal(self, root):
        stack = [root]

        nums = []

        while stack:
            node = stack.pop()
            nums.append(node.val)

            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return nums

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        nums = self.preorderTraversal(root)
        startNode = self.build_linkedlist(nums)

        # Print LinkedList
        nums_back = self.getback(startNode)
        print(nums_back)
    
        