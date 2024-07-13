"""
# Counting Sort()

Counting sort will be called as many time as Max number in the digit.

Count = len of base number system
Sorted = len of array

10 ** 0 = 1
10 ** 1 = 10
10 ** 2 = 100
10 ** 3 = 1000

Steps:
    1] Create a count datastructure - Decimal 10
    2] Count the number of times digit has occured
    3] Determine where to place elements in a partially sorted array
    4] Move in backward direction of the given array
    5] Copy the sorted array to main array
"""

def radixSort(array):
    # base case
    if len(array) <= 1:
        return array

    # get the max number form array
    maxNumber = max(array)
    # print("The max number is: ",maxNumber)


    # as long as we have elements in the max number keep performing counting sort
    # 8762 = 4
    digit = 0
    # print(maxNumber // 10 ** digit)
    while maxNumber // 10 ** digit > 0:
        # COUNT SORT
        countSort(array, digit)
        digit += 1
        print(maxNumber // 10 ** digit)
        
    return array

def countSort(array,digit):
    print(array)

    # Step 1: Initialize the data structure
    # creating a sorted array 
    sortedArray = [0] * len(array)

    # create a array that will hold the count
    # multiplying by 10. because we are using base 10 decimanl system
    '''
        We are sorting one digit at one time
        so a digit can go from 0 - 9
    '''
    countArray = [0] * 10

    #get the place of digit. eg. unit(1) 10 100 etc
    digitPlace = 10 ** digit

    print("\n")
    print("step 2: ")

    # Step 2: Count the number of times digit has occured
    for num in array:
        # Extract the digitplace element
        countIdx = (num // digitPlace ) % 10
        print("CountIdx = ",countIdx)
        # Increase the count value at the countArray
        countArray[countIdx] += 1
        
        print("CountArray",countArray)

    print("CountArray",countArray)
    print("\n")
    print("step 3: ")

    # Step 3: Determine where to place elements in a partially sorted array
    # Fill up the space so that we can keep adding the number before the sorted element
    for idx in range(1,10):
        '''
            array[i] = array[i-1] + array[i]
        '''
        countArray[idx] += countArray[idx - 1]
    print("CountArray",countArray)

    print("\n")
    print("step 4: ")

    # Step 4: Move in backwared direction
    for idx in range(len(array)-1, -1, -1):
        # print("idx: ", idx)
        # Take the digit number from the array
        countIdx = (array[idx] // digitPlace) % 10
        print("countIdx: ",countIdx)
        
        # Now subtract one number from countArray
        countArray[countIdx] -= 1
        
        # now add the array element at the position of the digitPlace in countArray
        sortedIdx = countArray[countIdx]
        print("sortedIdx: ", sortedIdx)
        sortedArray[sortedIdx] = array[idx]
        print("sortedArray",sortedArray)

    print("sortedArray",sortedArray)
        
    # step 5: copy the sorted array to main array
    for idx in range(len(array)):
        array[idx] = sortedArray[idx]


    return array