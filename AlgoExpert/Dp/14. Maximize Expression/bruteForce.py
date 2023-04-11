# Brute Force
# Tc: O(n^4) | Sc: O(1)

def maximizeExpression(array):
    n = len(array)

    if n < 4:
        return 0

    largest_val = float("-inf")

    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    a_val = array[a]
                    b_val = array[b]
                    c_val = array[c]
                    d_val = array[d]

                    cur_val = a_val - b_val + c_val - d_val

                    largest_val = max( largest_val , cur_val )

    return largest_val