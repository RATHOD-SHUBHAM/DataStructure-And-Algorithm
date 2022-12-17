# Tc: O(2 ^n) : for each n we are making 2 computation
# Sc: O(n) : for recursion stack
def getNthFib(n):
    # base condition
    if n == 1:
        return 0
    if n == 2:
        return 1
    # recursive condition
    return getNthFib(n - 1) + getNthFib(n - 2)