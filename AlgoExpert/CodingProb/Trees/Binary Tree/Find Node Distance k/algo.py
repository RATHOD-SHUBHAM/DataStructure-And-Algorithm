# This is an input class. Do not edit.
from collections import deque
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    parentNode_collection = {}
    getParentNode(tree , None, parentNode_collection)
    targetNode = getNodefromvalue(tree , target)
    return bfs(targetNode , k, parentNode_collection)

def getParentNode(root, parent, parentNode_collection):
    if not root:
        return

    parentNode_collection[root] = parent

    getParentNode(root.left, root, parentNode_collection)
    getParentNode(root.right, root, parentNode_collection)

    return

def getNodefromvalue(root, target):
    if not root:
        return None
        
    if root.value == target:
        return root

    leftNode = getNodefromvalue(root.left, target)
    rightNode = getNodefromvalue(root.right, target)

    return leftNode if leftNode is not None else rightNode

def bfs(targetNode , k, parentNode_collection):
    visited_node = set()
    queue = deque([(targetNode , 0)])
    result = []

    while queue:
        node , dist = queue.popleft()

        if node in visited_node:
            continue

        if dist == k:
            result.append(node.value)
            continue

        visited_node.add(node)

        if node.left:
            queue.append((node.left , dist + 1))

        if node.right:
            queue.append((node.right , dist + 1))

        if parentNode_collection[node]:
            queue.append((parentNode_collection[node] , dist + 1))

    return result
    
    
