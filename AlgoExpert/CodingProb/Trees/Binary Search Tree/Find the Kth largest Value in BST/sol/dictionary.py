# Time and space = O(h + k) and O(h)

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    dic = {
        "lastVisited" : 0,
        "totalVisited" : 0
    }
    return kClosest(tree, k ,dic)

def kClosest(root, k ,dic):
    if not root:
        return

    kClosest(root.right , k ,dic)

    if dic['totalVisited'] < k:
        dic['lastVisited'] = root.value
        dic['totalVisited'] += 1
        kClosest(root.left , k ,dic)

    return dic['lastVisited']