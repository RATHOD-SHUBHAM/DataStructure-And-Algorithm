# Running Product
# get the product of elements from both side up until current element.

#prod [i] = (up until left[i-1]) * (up until Right[i+1])

# Tc: O(n) | Sc: O(n)
def arrayOfProducts(array):
    n = len(array)
    prod = [1 for _ in range(n)]
    left_prod = [1 for _ in range(n)]
    right_prod = [1 for _ in range(n)]

    # get the left side product of all element until current ele
    runningProd = 1
    for i in range(n):
        left_prod[i] = runningProd # product until cur ele
        runningProd *= array[i] # get the product including cur ele

    # get the right side product of all element until current ele
    runningProd = 1
    for i in reversed(range(n)):
        right_prod[i] = runningProd
        runningProd *= array[i]

    # prod [i] = (up until left[i-1]) * (up until Right[i+1])
    for i in range(n):
        prod[i] = left_prod[i] * right_prod[i]
    # product of every number except itself

    return prod