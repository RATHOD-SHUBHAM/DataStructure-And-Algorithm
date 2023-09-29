# Tc: O(n) | Sc: O(1)

def arrayOfProducts(array):
    n = len(array)

    # left_running_prod = [1] * n
    # right_running_prod = [1] * n
    running_p_ = [1] * n

    # calculate the running prod form left to right
    running_prod = 1
    for i in range(n):
        # Insted of storing in seperate array, store it in one array
        # left_running_prod[i] = running_prod
        running_p_[i] = running_prod

        # calculate the running product
        running_prod *= array[i]

    # print(left_running_prod)
    print(running_p_)

    # calculate the running prod form right to left
    # Directly grab value form final array and save it back.
    running_prod = 1
    for i in reversed(range(n)):
        # right_running_prod[i] = running_prod
        running_p_[i] *= running_prod

        # calculate the running product
        running_prod *= array[i]

    # print(right_running_prod)

    # calculate the final prod
    
    # for i in range(n):
    #     running_p_[i] = left_running_prod[i] * right_running_prod[i]

    # print(running_p_)
    return running_p_
