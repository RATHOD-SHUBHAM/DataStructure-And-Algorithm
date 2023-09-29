'''
    Steps:
        1. Calculate the left running sum.
        2. Calculate the right running sum.
        3. Calculate the final product.
'''

# Tc Sc: O(n)

def arrayOfProducts(array):
    n = len(array)

    left_running_prod = [1] * n
    right_running_prod = [1] * n

    # calculate the running prod form left to right
    running_prod = 1
    for i in range(n):
        left_running_prod[i] = running_prod

        # calculate the running product
        running_prod *= array[i]

    print(left_running_prod)

    # calculate the running prod form right to left
    running_prod = 1
    for i in reversed(range(n)):
        right_running_prod[i] = running_prod

        # calculate the running product
        running_prod *= array[i]

    print(right_running_prod)

    # calculate the final prod
    running_p_ = [1] * n
    for i in range(n):
        running_p_[i] = left_running_prod[i] * right_running_prod[i]

    print(running_p_)
    return running_p_
