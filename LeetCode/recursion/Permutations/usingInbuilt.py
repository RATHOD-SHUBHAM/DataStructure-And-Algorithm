# https://stackoverflow.com/questions/53419536/what-is-the-computational-complexity-of-itertools-combinations-in-python

# TIme Complexity: O(n!)
# Space Complexity: O(n!)
'''
Time Complexity graph for itertools.permutation

It is observed that the time complexity is O(n!), 
where n = Input Size

'''
from itertools import permutations
def getPermutations(array):
	if len(array) < 1:
		return array
    return (list(permutations(array)))