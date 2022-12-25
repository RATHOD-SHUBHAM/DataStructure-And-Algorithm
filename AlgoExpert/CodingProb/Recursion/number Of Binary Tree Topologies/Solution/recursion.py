def numberOfBinaryTreeTopologies(n):
    # base case
    if n == 0:
        return 1

    # consider leftsubtree to start from 0
    topology_count = 0
    for leftsubtree in range(n):
        rightsubtree = n - 1 - leftsubtree

        leftsubtree = numberOfBinaryTreeTopologies(leftsubtree)
        rightsubtree = numberOfBinaryTreeTopologies(rightsubtree)
        topology_count += leftsubtree * rightsubtree

    return topology_count