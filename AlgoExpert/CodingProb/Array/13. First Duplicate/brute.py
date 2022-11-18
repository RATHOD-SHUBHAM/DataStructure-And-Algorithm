# Tc and Sc: O(n)
def firstDuplicateValue(array):
    # Write your code here.
    dict = {}

    for i in range(len(array)):
        if array[i] in dict:
            return array[i]
        dict[array[i]] = i

    return -1
