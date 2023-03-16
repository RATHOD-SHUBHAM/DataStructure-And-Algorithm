'''
						 node depth of left subtree + no of node on left subtree 
sum of all nodes depth =								+
						 node depth of right subtree + no of nodes on right subtree
'''	
def allKindsOfNodeDepths(root):
    nodeCount = {}
    no_of_nodes(root, nodeCount)
    print(nodeCount)

    nodeDepth = {}
    depth_of_node(root, nodeCount, nodeDepth)
    print(nodeDepth)

    return all_kind_of_node_depth(nodeDepth)


def no_of_nodes(root, nodeCount):
    nodeCount[root] = 1

    if root.left:
        no_of_nodes(root.left, nodeCount)
        nodeCount[root] += nodeCount[root.left]

    if root.right:
        no_of_nodes(root.right, nodeCount)
        nodeCount[root] += nodeCount[root.right]

    return

'''
						 node depth of left subtree + no of node on left subtree 
sum of all nodes depth =								+
						 node depth of right subtree + no of nodes on right subtree
'''	
def depth_of_node(root, nodeCount, nodeDepth):
    # base case
    nodeDepth[root] = 0

    if root.left:
        depth_of_node(root.left, nodeCount, nodeDepth)
        nodeDepth[root] += nodeDepth[root.left] + nodeCount[root.left]

    if root.right:
        depth_of_node(root.right, nodeCount, nodeDepth)
        nodeDepth[root] += nodeDepth[root.right] + nodeCount[root.right]

    return


def all_kind_of_node_depth(nodeDepth):
    all_node_depth = 0
    for val in nodeDepth.values():
        all_node_depth += val

    return all_node_depth

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
