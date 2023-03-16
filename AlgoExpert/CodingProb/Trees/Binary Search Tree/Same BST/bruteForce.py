# Tc and Sc: (n^2)
def sameBsts(arrayOne, arrayTwo):
    # Base Case
    if not arrayOne and not arrayTwo:
        return True

    if not arrayOne or not arrayTwo:
        return False

    # if the nodes are not the same
    rootOne = arrayOne[0]
    rootTwo = arrayTwo[0]
    if rootOne != rootTwo:
        return False

    # divide the array into left and right half
    leftSubtree_one = smallerThanRoot(arrayOne, rootOne)
    rightSubtree_one = greaterThanRoot(arrayOne, rootOne)
    
    # print("leftSubtree_one: ",leftSubtree_one)
    # print("rightSubtree_one : ",rightSubtree_one)

    leftSubtree_two = smallerThanRoot(arrayTwo, rootTwo)
    rightSubtree_two = greaterThanRoot(arrayTwo, rootTwo)

    # print("leftSubtree_two: ",leftSubtree_two)
    # print("rightSubtree_two : ",rightSubtree_two)

    # once we get the left and right half - compare them
    leftChild = sameBsts(leftSubtree_one, leftSubtree_two)
    rightChild = sameBsts(rightSubtree_one, rightSubtree_two)

    return leftChild and rightChild

    
def smallerThanRoot(array, root):
    smallerArray = [] # stores all the node smaller then root

    for i in range(1, len(array)): # array[0] will be root node
        child = array[i]
        
        if child < root:
            smallerArray.append(child)

    return smallerArray


def greaterThanRoot(array, root):
    greaterArray = []

    for i in range(1, len(array)): # array[0] will be root node
        child = array[i]

        if child >= root:
            greaterArray.append(child)

    return greaterArray