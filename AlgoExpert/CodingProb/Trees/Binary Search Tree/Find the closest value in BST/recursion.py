# Tc and Sc: O(n)

import math
def findClosestValueInBst(tree, target):
    # closest = [difference, node]
    closest = [math.inf, tree.value]
    closestNode(tree, target, closest)
    return closest[1]

def closestNode(node, target, closest):
    if not node:
        return
    
    # calculate the closest value
    curVal = abs(node.value - target)
    if curVal < closest[0]:
        # the difference
        closest[0] = curVal
        # the node
        closest[1] = node.value

    # Check the direction to go
    if target > node.value:
        return closestNode(node.right, target, closest)

    if target < node.value:
        return closestNode(node.left, target, closest)
        
    


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
