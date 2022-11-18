'''

# Running Product

Write a function that thats in a non-empty array of integers and 
return an array of same length, where each element in the output array is 
equal to the product of every other number in the input array.

eg:
ip_array = [5,1,4,2,6]
op_array = [48,240,60,120,40]

'''

# brute force
# Tc: O(n^2) | Sc: O(n)

def arrayOfProducts(array):
    n = len(array)
    op = []

    for i in range(n):
        runningProd = 1
        for j in range(n):
            if i == j:
                continue
            runningProd *= array[j]
        op.append(runningProd)
    return op

