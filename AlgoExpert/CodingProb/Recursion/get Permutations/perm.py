# backtrack method

def getPermutations(array):
    if not array:
        return array
        
    perm = []
    prev_perm = []
    return backtrack(prev_perm, perm, array)

def backtrack(prev_perm, perm, array):
    # todo: base case
    if len(array) == 0:
        perm.append(prev_perm)
        return
    # for each idx - check the permutations
    for i in range(len(array)):
        cur_perm = prev_perm + [array[i]]
        new_array = array[ : i] + array[i + 1 : ]
        backtrack(cur_perm, perm, new_array)

    return perm
