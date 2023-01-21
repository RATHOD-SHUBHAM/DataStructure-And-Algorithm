# brute force iterative approach
import math
def findClosestValueInBst(tree, target):
    closest = [math.inf, math.inf]
    stack = [tree]

    while stack:
        node = stack.pop()

        if node is None:
            break

        curVal = abs(target - node.value)

        if curVal < closest[0]:
            closest[0] = curVal
            closest[1] = node.value

        if target > node.value:
            stack.append(node.right)
        elif target < node.value:
            stack.append(node.left)
        else:
            break
    
    return closest[1]


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
