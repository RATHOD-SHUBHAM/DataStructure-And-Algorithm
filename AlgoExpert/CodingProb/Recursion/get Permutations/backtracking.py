def getPermutations(array):
    result = []
    n = len(array)

    # when there is only one element return that element
    if n == 1:
        return [array[:]]

    # loop for n time
    for i in range(n):
        
        # remove an elemnt from front
        parent_ele = array.pop(0)
        
        # get permutation of remaining array. as parent ele will be popped
        permutation = getPermutations(array)
        print("permutation: ",permutation)

        # to the permuation obtained add the parent ele
        # sometimes we will have multiple permutation
        for perm in permutation:
            perm.append(parent_ele)
            print("perm: ",perm)
        print("permutation: ",permutation)

        # put the parent ele back into array to get the next combination set
        array.append(parent_ele)

        # appending will make it [] + [[]] =  [[[]]]
        # extending will add to existing list [] + [[]] = [[]]
        result.extend(permutation)
        print(result)
        print("\n")

    return result