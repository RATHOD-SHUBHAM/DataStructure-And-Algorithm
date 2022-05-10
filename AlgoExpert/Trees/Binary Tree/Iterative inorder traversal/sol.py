'''
Morris Traversal

            1                    1
           /  \                  |  \
          7    4    =>       7   |    4       
         / \  / \           | \  |    | \
        8  9 5   6        8--  9--  5-   6


Steps:

1] When cur node has a left child:
    1. move to the right most child of left child and make it point to cur node
    2. remove the connection between left and cur node . in order to avoid revisiting the left child over and over again

Inorder to do so. 
    - have 2 pointer next and prev
    * let the next node travel to right most child of left node  
        next.right == curnode 
        eg 9 will be pointing to 1
    * now we got to go left. but before going left delete the curNode left pointer
        prevNode = curNode
        curnode = curnode.left
        prevNode = None
    


2] if curNode doesnot have left child:
    1. add cur node to result
    2. then move to right child

'''

# Time : O(n)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curNode = root
        nextNode = None
        prevNode = None
        
        while curNode:
            # if there is no left node. add the curNode value to res and go right
            if not curNode.left:
                res.append(curNode.val)
                curNode = curNode.right
            else:
                nextNode = curNode.left
                # travel to right most node of left childe and make it point to root node
                while nextNode.right:
                    nextNode = nextNode.right
                    
                # pointing to root node
                nextNode.right = curNode
                
                # keeping track of curNode
                prevNode = curNode
                #moving curNode to left
                curNode = curNode.left
                
                # removing root node pointer to left as we dont want to revisit left child
                prevNode.left = None
        
        return res
        