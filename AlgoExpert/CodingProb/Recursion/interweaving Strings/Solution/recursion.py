# Tc: O (2^(one + two)) , Sc:O(one + two)

def interweavingStrings(one, two, three):
    # base case
    if len(three) != len(one) + len(two):
        return False

    i = 0
    j = 0

    return backtrack(i , j, one, two, three)

def backtrack(i , j, one, two, three):
    k = i + j
    
    # base case: when k moves out of string three. it has sucessfully completed all comparison
    if k == len(three):
        return True

    # check the current value with i
    if i < len(one) and one[i] == three[k]:
        # move to the next value of i
        if backtrack(i + 1 , j, one, two, three):
            return True

    # if i is false then check with j value
    if j < len(two) and two[j] == three[k]:
        if backtrack(i, j+1, one, two, three):
            return True

    # if both the value dont match, return false
    return False
            
    
