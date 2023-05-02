# Tc :O(n^3) | Sc: O(n^2)

def juiceBottling(prices):
    n = len(prices)

    profit = [0] * n
    sequence = [[]] * n

    for quantity in range(n):
        for prevQuantity in range(quantity + 1):
            # get the remaining quantity if i use up the previous quantity
            # a + b = x -> x - a = b -> quantity = prevQuantity +  remainingQuantity -> remainingQuantity = quantity - prevQuantity
            remainingQuantity = quantity - prevQuantity
            
            cur_profit = prices[prevQuantity] + profit[remainingQuantity]

            if cur_profit > profit[quantity]:
                profit[quantity] = cur_profit
                sequence[quantity] = [prevQuantity] + sequence[remainingQuantity]

    return sequence[-1]