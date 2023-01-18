# Tc: O(n) | Sc: O(1)

def findClosestValueInBst(tree, target):
    closest = tree.value
    return closestNode(tree, closest, target)

def closestNode(tree, closest, target):
    curNode = tree

    while curNode:
        
        if abs(target - curNode.value) < abs(target - closest):
            closest = curNode.value
        
        if target == curNode.value:
            break
            
        elif target > curNode.value:
            curNode = curNode.right

        elif target < curNode.value:
            curNode = curNode.left

    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
