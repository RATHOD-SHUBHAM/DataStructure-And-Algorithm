# Complete the reverseArray function below.
def reverseArray(a):
    # O(n) and space O(1)
    #return(a[::-1])
    #or
    # O(n) and space O(n)
    new_arr = []
    for i in reversed(range(len(a))):
        new_arr.append(a[i])
    return new_arr