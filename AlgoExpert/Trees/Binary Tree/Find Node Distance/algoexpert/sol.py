# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# here target is a integer value and in leetcode target is a node.
def findNodesDistanceK(tree, target, k):
    ans = []
	helper(tree,target,k,ans)
	return ans

def helper(root,target,k,ans):
	if not root:
		return -1
	elif root.value == target:
		subTree(root,k,ans,0)
		return 1
	else:
		leftTree = helper(root.left,target,k,ans)
		rightTree = helper(root.right,target,k,ans)
		
		if leftTree != -1:
			if leftTree == k:
				ans.append(root.value)
			else:
				subTree(root.right,k,ans,leftTree + 1)
			return leftTree + 1
		
		elif rightTree != -1:
			if rightTree == k:
				ans.append(root.value)
			else:
				subTree(root.left,k,ans,rightTree + 1)
			return rightTree + 1
		
		else:
			return -1
		
def subTree(root,k,ans,curDist):
	if not root:
		return
	elif curDist == k:
		ans.append(root.value)
	else:
		subTree(root.left,k,ans,curDist+1)
		subTree(root.right,k,ans,curDist+1)
