# associate each value with a index:
# since each array range from [1 - n]
# we can associate 1 - index 0, 2 - index 1, 3 - index 2 and so on
# now when a number repeats , we will look at the value at associated index.
# if the flag has changed then the value is a duplicate

def firstDuplicateValue(array):
    n = len(array)

    for i in range(n):
        value = array[i]
        
        idx = abs(value) - 1 # associate index to each value

        # check the flag at the index to check if the current value was prev seen
        if array[idx] < 0:
            return abs(value)

        # flip the flag value
        array[idx] *= -1 

    return -1
        
    
