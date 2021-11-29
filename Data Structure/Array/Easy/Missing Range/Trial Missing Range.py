'''
nums = sorted and Unique
missing = When X is in the range but not in nums

nums = 0 - 100
lower <= nums <= upper

'''





'''

result = []

lower = 0, upper = 99

nums = [ 0, 1, 3, 50, 75]
               i 

i - lower = 0
increase i and lower by 1


lower = 1
 Check i - (i-1) = 1:
    i - lower = 0:
    increase i and lower by 1

lower = 2
i - (i-1) != 1:
    if (i - 1) - lower == 0:
        result = ["lower"] # result = ["2"]
        increase i
        lower = i + 1

lower = 4
if (i - 1) - lower != 0:
    result = ["lower - (i-1)] # result = ["2","4 - 49"]
    increase i
    lower = i + 1

lower = 51
if (i - 1) - lower != 0:
    result = ["lower - (i-1)] # result = ["2","4 - 49", "51 - 74"]
    increase i
    lower = i + 1

lower = 76
if i is out of range:
    if lower == upper:
        result = ["lower"]
    else:
        result = ["lower - upper"] # result = ["2","4 - 49", "51 - 74", "76 - 99"]

'''






'''
# case 2
lower = 1, upper = 1
nums = [], 
        i


if i == None:
    if lower == upper:
        result = ["lower"] # result = ["1"]

'''





'''
# case 3
nums = [], lower = -3, upper = -1
if i == None:
    if lower == upper:
        result = ["lower"] # result = ["1"]
    else:
        result = ["lower - upper"] # result = ["-3 - -1"]

'''





'''
# case 4
nums = [-1], lower = -1, upper = -1

i - lower = 0
    if lower == upper:
        return []

'''





'''

# case 5

lower = -2, upper = -1 
nums = [-1], 

-1 - (-2) = 1
if i - lower != 0:
    result = ["lower - (i-1)] # result = ["-2 - -1"]


i - lower = 0
increase i and lower by 1


lower = 1
 Check i - (i-1) = 1:
    i - lower = 0:
    increase i and lower by 1

lower = 2
i - (i-1) != 1:
    if (i - 1) - lower == 0:
        result = ["lower"] # result = ["2"]
        increase i
        lower = i + 1

lower = 4
if (i - 1) - lower != 0:
    result = ["lower - (i-1)] # result = ["2","4 - 49"]
    increase i
    lower = i + 1

lower = 51
if (i - 1) - lower != 0:
    result = ["lower - (i-1)] # result = ["2","4 - 49", "51 - 74"]
    increase i
    lower = i + 1

lower = 76
if i is out of range:
    if lower == upper:
        result = ["lower"]
    else:
        result = ["lower - upper"] # result = ["2","4 - 49", "51 - 74", "76 - 99"]

'''


# ================================================================================


'''
OR

lower = -1 upper = 15
nums = [1, 2, 4, 10, 12]
                         i
check if my number is between lower and upper bound

if i == 0:
    if nums[i] != lower:
        result = ["lower -> nums[i]-1"] # result = ["-1 -> 0"]
        increase i

if i - (i-1) != 1:
    if nums[i]-1 == nums[i-1]+1:
        result = ["nums[i-1]+1"] # result = ["-1 -> 0","3"] result = ["-1 -> 0","3","5 -> 9","11"]
        increase i
    elif nums[i]-1 != nums[i-1]+1:
        result = ["nums[i-1]+1 -> nums[i]-1"] # result = ["5 -> 9"]
        increase i
else:
    increase i

if i is out of range:
    if i-1 != upper:
        result = ["nums[i-1]+1 -> upper"] # result = ["-1 -> 0","3","5 -> 9","11","13 -> 15"]


'''

# ================================================================================

'''




'''