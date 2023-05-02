# Tc and Sc: O(n)

# store the current largest value up until that index
import math
def maximizeExpression(array):
    n = len(array)

    if n < 4:
        return 0

    # store maximum value of A
    max_of_A = [-math.inf] * n

    # store the value of A - B
    max_of_A_minus_B = [-math.inf] * n

    # store the value of A - B + C
    max_of_A_minus_B_plus_C = [-math.inf] * n

    # store the value of A - B + C - D
    max_of_A_minus_B_plus_C_minus_D = [-math.inf] * n

    # calculate max of A
    for i in range(n):
        curVal = array[i]
        max_of_A[i] = max(max_of_A[i - 1] , curVal)

    # print(max_of_A)

    # calculate A - B
    for i in range(1 , n):
        cur_B = array[i]

        # get max A value till the prev index
        prevMax = max_of_A[i - 1]
        curVal = prevMax - cur_B
        
        max_of_A_minus_B[i] = max(max_of_A_minus_B[i - 1] , curVal)

    # print(max_of_A_minus_B)


    # Calculate A - B + C
    for i in range(2 , n):
        cur_C = array[i]

        # get max A - B value till the prev index
        prevMax = max_of_A_minus_B[i - 1]
        curVal = prevMax + cur_C
        
        max_of_A_minus_B_plus_C[i] = max(max_of_A_minus_B_plus_C[i - 1] , curVal)

    # print(max_of_A_minus_B_plus_C)

    # Calculate A - B + C - D
    for i in range(3 , n):
        cur_D = array[i]

        # get max A - B value till the prev index
        prevMax = max_of_A_minus_B_plus_C[i - 1]
        curVal = prevMax - cur_D
        
        max_of_A_minus_B_plus_C_minus_D[i] = max(max_of_A_minus_B_plus_C_minus_D[i - 1] , curVal)

    # print(max_of_A_minus_B_plus_C_minus_D)

    return max_of_A_minus_B_plus_C_minus_D[-1]
    
