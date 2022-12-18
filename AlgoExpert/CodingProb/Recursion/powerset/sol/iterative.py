# Tc: O(2^n * n)
def powerset(array):
    subset = [[]]
    n = len(array)
    
    # O(n) for all element
    for i in range(n):
        m = len(subset)

        # O(2^n) : Permutation
        for j in range(m):
            cur_val = array[i]
            
            # get values in current subset
            subset_val = subset[j]
            print(subset_val)

            new_subset = subset_val + [cur_val]
            print(new_subset)
            

            subset.append(new_subset)
            print(subset)
            print("\n")

    return subset

            
