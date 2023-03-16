# Time = O(n!)
# Space = O(n!)

from itertools import permutations
def getPermutations(array):
    if not array:
        return array
    # Write your code here.
    return list(permutations(array))
