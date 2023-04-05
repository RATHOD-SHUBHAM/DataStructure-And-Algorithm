# n is number of item and c is capacity
# Tc and Sc: O(n*c)

def knapsackProblem(items, capacity):
    # base case - inital row is zero because there is no items to add
    dp = [[0]*(capacity + 1) for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        # value of current item
        curItem = items[i-1][0]

        # weight of current item
        curWeight = items[i-1][1]

        for j in range(1, capacity + 1):
            # knapsack weights = j
            if curWeight > j:
                # cannot add items: cannot fit large item in smaller bag
                dp[i][j] = dp[i-1][j]
            else:
                # add max (what ever the item price up until now or (curItem + item price before adding the current weight) )
                # item cost before adding the current price = dp[i-1][j - curWeight]
                # item price up until now = dp[i-1][j]
                totalItemCost = curItem + dp[i-1][j - curWeight]
                costUntilnow = dp[i-1][j]
                dp[i][j] = max(costUntilnow, totalItemCost)

    # print(dp)
    max_total_val = dp[-1][-1]
    return [max_total_val, knapsack_item(dp, items)]

def knapsack_item(dp, items):
    sequence = []
    
    i = len(dp) - 1
    j = len(dp[0]) - 1

    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            # not piking the current value
            i -= 1
        else:
            # picking up the current value. so add its index
            sequence.append(i-1)
            # carefull - if i change my i value before this then my j value will go wrong
            j = j - items[i-1][1]
            i -= 1
            

    # print(sequence)
    return sequence[::-1]