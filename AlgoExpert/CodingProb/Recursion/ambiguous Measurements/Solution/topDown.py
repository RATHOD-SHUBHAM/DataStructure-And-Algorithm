# cup limit should be in between low and high . for the cup to make measurment
# Top Down
def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    memo = set() # keep track of the volume that cannot be measured
    cup_low = 0
    cup_high = 0
    return recursion(measuringCups, low, high, cup_low, cup_high, memo)

def recursion(measuringCups, low, high, cup_low, cup_high, memo):
    key = (cup_low , cup_high)
    if key in memo:
        return False
    
    # base case
    # 2 cases where the range cant be measured

    # case 1: when cup low is above the range of high
    if cup_low > high :
        memo.add(key)
        return False

    # case 2: when cup high goes above the range of high
    if high < cup_high:
        memo.add(key)
        return False

        
    # when the cup can measure the range
    if low <= cup_low and cup_high <= high:
        return True

    # both low and high of cup are small than low and high
    # try different combination of cup to enter the given range
    for cup in measuringCups:
        cupLow, cupHigh = cup

        # if with any combination we enter the range, return True
        if recursion(measuringCups, low, high, cup_low + cupLow, cup_high + cupHigh, memo):
            return True

    # with this value we cannot find the range
    memo.add(key)
    return False