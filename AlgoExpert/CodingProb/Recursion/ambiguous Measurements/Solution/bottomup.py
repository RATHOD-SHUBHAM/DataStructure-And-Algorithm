# cup limit should be in between low and high . for the cup to make measurment
# bottom up
def ambiguousMeasurements(measuringCups, low, high):
    memo = set() # keep track of the level that cannot be measured

    return backtracking(memo, measuringCups, low, high)

def backtracking(memo, measuringCups, low, high):
    # At some point the limit will zero, hence cant be measured
    if low < 0 and high < 0:
        return False

    current_level = (low, high)

    # if this level cannot be measured
    if current_level in memo:
        return False

    # measure with different cup
    for cups in measuringCups:
        cup_lower_level, cup_upper_level = cups

        # This is the only condition where limit can be measured
        if low <= cup_lower_level and cup_upper_level <= high:
            return True

        # if cant be measured , reduce the limit and check
        if backtracking(memo, measuringCups, low - cup_lower_level , high - cup_upper_level):
            return True

    # after all the cups are compared and we come out of for loop means
    # none of the cups were able to measure the given limit
    memo.add(current_level)
    return False
