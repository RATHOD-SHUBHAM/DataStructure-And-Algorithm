def powerset(array):
    subsets = []

    cur_subset = []
    def dfs(idx):
        n = len(array)
         # base case
        if idx >= n:
            # add the copy, because we need to manipulate the cur_subset even further
            subsets.append(cur_subset[:])
            return subsets
    
        # add the current element, and move to next element
        cur_subset.append(array[idx])
        dfs(idx + 1)
    
        # dont add the current element and move to next element
        cur_subset.pop()
        dfs(idx + 1)


    # function call
    idx = 0
    dfs(idx)
    return subsets
