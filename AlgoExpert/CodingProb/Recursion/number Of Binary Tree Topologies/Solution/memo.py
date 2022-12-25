memo = {
    0 : 1
}
def numberOfBinaryTreeTopologies(n):
    global memo

    # base case
    if n in memo:
        return memo[n]

    # consider leftsubtree to start from 0
    topology_count = 0
    for leftsubtree in range(n):
        rightsubtree = n - 1 - leftsubtree

        memo[leftsubtree] = numberOfBinaryTreeTopologies(leftsubtree)
        memo[rightsubtree] = numberOfBinaryTreeTopologies(rightsubtree)
        topology_count += memo[leftsubtree] * memo[rightsubtree]

    memo[n] = topology_count
    return memo[n]