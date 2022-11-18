# a little bit clever solution
# insted of left and right array - multiply directly to prod on run


# Tc: O(n) | Sc: O(n)
def arrayOfProducts(array):
    n = len(array)
    prod = [1 for _ in range(len(array))]

    # get the left side product of all element until current ele
    runningProd = 1
    for i in range(n):
        prod[i] = runningProd # product until cur ele
        runningProd *= array[i] # get the product including cur ele

    # get the right side product of all element until current ele
    # Multiply directly to prod insted on new array
    runningProd = 1
    for i in reversed(range(n)):
        prod[i] *= runningProd # product until cur ele
        runningProd *= array[i] # get the product including cur ele

    return prod
