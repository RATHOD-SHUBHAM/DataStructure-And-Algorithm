# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# Tc and Sc : O(n)        
# bottom to top recursion
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestoral_history = set() # keep track of the ancestor

    # get all  the ancestor of descendantOne
    while descendantOne:
        ancestoral_history.add(descendantOne.name)
        # if there is no ancestor then we reached the top - break
        if not descendantOne.ancestor:
            break
        descendantOne = descendantOne.ancestor

    # print(descendantOne.name)
    # print("ancestoral_history: ", ancestoral_history)

    # get the ancestor of descendantTwo
    while descendantTwo:
        # if at any point we come across a ancestor that is already present in set
        # mean we have found the common ancestor
        if descendantTwo.name in ancestoral_history:
            return descendantTwo

        # ancestoral_history.add(descendantTwo.name)
        if not descendantTwo.ancestor:
            break
            
        descendantTwo = descendantTwo.ancestor