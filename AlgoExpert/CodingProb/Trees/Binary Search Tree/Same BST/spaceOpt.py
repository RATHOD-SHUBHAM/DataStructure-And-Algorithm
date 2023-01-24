'''
# for left child
 * parentNode <= rightChild < AncestorNode

# for right child
    * parentNode > leftChild >= AncestorNode
'''
def sameBsts(arrayOne, arrayTwo):
    minAncestor = float("-inf")
    maxAncestor = float("inf")
    rootOneIdx = 0
    rootTwoIdx = 0
    return checkSameBST(arrayOne, arrayTwo, rootOneIdx, rootTwoIdx, minAncestor, maxAncestor)

def checkSameBST(arrayOne, arrayTwo, rootOneIdx, rootTwoIdx, minAncestor, maxAncestor):
    # base case
    # when we reach the end - check if both the indexs are outside 
    # by checking if both are pointing to same idx
    if rootOneIdx == -1 or rootTwoIdx == -1:
        return rootOneIdx == rootTwoIdx
        
    # check if the nodes are not same
    if arrayOne[rootOneIdx] != arrayTwo[rootTwoIdx]:
        return False

    # get the next smaller and largest element -- this will form the left and right subtree node
    leftChildNode_one = getNextSmaller(arrayOne, rootOneIdx, minAncestor)
    rightChildNode_one = getNextLarger(arrayOne, rootOneIdx, maxAncestor) 

    
    leftChildNode_Two = getNextSmaller(arrayTwo, rootTwoIdx, minAncestor)
    rightChildNode_Two = getNextLarger(arrayTwo, rootTwoIdx, maxAncestor)
    

    # arrayOne and arrayTwo - root node will have same value
    ancestorNode = arrayOne[rootOneIdx]
    
    # all the value in left subtree should be less than its parentNode.
    leftSubTree = checkSameBST(arrayOne, arrayTwo, leftChildNode_one, leftChildNode_Two, minAncestor, ancestorNode)
    
    # all the value in right Subtree should be greater than its parentNode
    rightSubTree = checkSameBST(arrayOne, arrayTwo, rightChildNode_one, rightChildNode_Two, ancestorNode, maxAncestor)

    return leftSubTree and rightSubTree

# minAncestor is useless for left child
# its useful for finding rightchild's left child
def getNextSmaller(array, rootIdx, minAncestor):
    for i in range(rootIdx + 1, len(array)):
        if array[i] < array[rootIdx]:
            # if for rightchild - we are looking for left child
            if array[i] >= minAncestor:
                return i
    return -1

def getNextLarger(array, rootIdx, maxAncestor):
    for i in range(rootIdx + 1, len(array)):
        if array[i] >= array[rootIdx]:
            # maxAncestor is only useful for leftchilds- right child
            if array[i] < maxAncestor:
                return i
    return -1