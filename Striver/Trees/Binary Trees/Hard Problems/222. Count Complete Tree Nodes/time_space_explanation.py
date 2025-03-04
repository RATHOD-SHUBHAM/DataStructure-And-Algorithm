'''
# Width of the Tree

Time Complexity: O(n)

The code performs a level-order traversal (breadth-first search) of the binary tree.
Each node is visited exactly once during the traversal.
For each node, the algorithm does constant-time operations:

Checking if the node has left or right children
Calculating positions
Appending children to the queue


The while loop runs until the queue is empty, which means it processes all nodes in the tree.
Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity: O(w), where w is the maximum width of the tree

The space complexity is determined by the queue used for level-order traversal.
In the worst case, the queue will hold nodes from the widest level of the tree.
For a complete binary tree, the maximum width occurs at the last level.
The maximum number of nodes at the last level can be (n+1)/2 for a complete binary tree, where n is the total number of nodes.
So the space complexity is O(w), which is effectively O(n) in the worst case.


The code is interesting because it not only counts nodes but also tracks their relative positioning, which could be useful for problems involving tree width or level-based node counting.


'''



'''
# Height of the Tree
Time Complexity: O(log²n)

The algorithm uses a clever approach to count nodes in a binary tree, particularly optimized for complete binary trees.
height_of_lefttree() and height_of_righttree() methods take O(log n) time, as they traverse down to the leftmost or rightmost path of the tree.
The recursive approach has an interesting optimization:

For a complete or perfect binary tree, it can calculate the number of nodes in O(log n) time by using the formula (2^h) - 1
For an incomplete tree, it recursively breaks down the problem
The recursion depth is at most log n (height of the tree)


Each recursive call makes two height calculations (left and right subtree heights)
This leads to a time complexity of O(log²n)

Space Complexity: O(log n)

The space complexity is determined by the recursion stack
The maximum depth of recursion is log n (the height of the tree)
Each recursive call uses constant extra space
The height calculation methods use iterative approaches with O(1) extra space
Therefore, the space complexity is O(log n)


# Solution
So basically , For every node we check if the node is a perfect binary tree
if it is a perfect binary tree we apply the fomula to find the total number of nodes in the tree ((2^h) - 1).
else, we recursively check if left or right subtree is a perfect binary tree or not.
The we add current node count to the perfect binary tree that was returned.

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.completeBT(root)
    
    def completeBT(self, root):
        if not root:
            return 0
        
        leftTreeHeight = self.perfectBT_left(root)
        rightTreeHeight = self.prefectBT_right(root)

        if leftTreeHeight == rightTreeHeight:
            return 2 ** rightTreeHeight - 1
        else:
            leftTree = self.completeBT(root.left)
            rightTree = self.completeBT(root.right)

            return 1 + leftTree + rightTree
        
    def perfectBT_left(self, root):
        count = 0

        while root:
            count += 1
            root = root.left
        return count
    
    def prefectBT_right(self, root):
        count = 0

        while root:
            count += 1
            root = root.right
        return count

'''