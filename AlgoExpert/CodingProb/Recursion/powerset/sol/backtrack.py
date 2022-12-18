def powerset(array):
    subsets = []  
    cur_subset = []
    idx = 0
    n = len(array)
    return dfs(idx , n , array, cur_subset, subsets)

def dfs(idx , n , array, cur_subset, subsets):
    # base case
    if idx >= n:
        # add the copy, because we need to manipulate the cur_subset even further
        subsets.append(cur_subset[:])
        return subsets

    # add the current element, and move to next element
    cur_subset.append(array[idx])
    dfs(idx + 1, n , array, cur_subset, subsets)

    # dont add the current element and move to next element
    cur_subset.pop()
    dfs(idx + 1, n , array, cur_subset, subsets)

    return subsets
    
