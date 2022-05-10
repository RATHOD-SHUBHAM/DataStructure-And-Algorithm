# Time and space = O(n) where n is the number of nodes in the tree

'''

Traverse in 2 direction
        3
       / \
      5   1
     / \  / \
    6   2 0  8
       / \
      7   4

if target is 5. get subnode for 5 from its children
also return to parent and get siblings node with distance k from it

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        ans = []
        self.helper(root,ans, target, K)
        return ans
    
    def helper(self, root, ans, target, K):
        if not root:
            return -1
        # if the target node is found
        elif root == target:
            # get the nodes from subtree with distance k
            self.subtreeNodes_dist_k(root,0,K,ans)
            return 1 # return this to parent as parent is at distance 1
        else:
            leftTree = self.helper(root.left,ans, target, K)
            rightTree = self.helper(root.right,ans, target, K)
            
            # if the node is found on left sub tree then leftTree val will not be -1 anymore
            if leftTree != -1:
                # if parent is at distance k
                if leftTree == K:
                    ans.append(root.val)
                else:
                    # if node is on left side then go right from parent to get node with distance k
                    self.subtreeNodes_dist_k(root.right,leftTree+1,K,ans)
                # return distance + 1 to ancestor node if present
                return leftTree + 1
            
            elif rightTree != -1:
                if rightTree == K:
                    ans.append(root.val)
                else:
                    self.subtreeNodes_dist_k(root.left,rightTree+ 1,K,ans)
                return rightTree + 1
            
            else:
                return -1
        
        
    def subtreeNodes_dist_k(self,root,curDist,K,ans):
        if not root:
            return
        elif curDist == K:
            ans.append(root.val)
        else:
            self.subtreeNodes_dist_k(root.left,curDist+1,K,ans)
            self.subtreeNodes_dist_k(root.right,curDist+1,K,ans)
        