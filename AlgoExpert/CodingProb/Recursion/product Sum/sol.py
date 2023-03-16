# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# Tc and Sc: O(n)


# pass the depth
# initial depth = 1
def productSum(array,depth = 1):
    # Write your code here.
    summ = 0
    for ele in array:
        # check if the type is list
        if type(ele) is list:
            # if type is list get the sum of that list and increase depth
            summ += productSum( ele , depth + 1)
        else:
            summ += ele
    # product sum
    return summ * depth
