# Tc :O(n^2) | Sc: O(n)

def juiceBottling(prices):
    n = len(prices)

    profit = [0] * n
    sequence = [0] * n # this will tell us which bottle we consumed

    for quantity in range(n):
        for prevQuantity in range(quantity + 1):
            # get the remaining quantity if i use up the previous quantity
            # a + b = x -> x - a = b -> quantity = prevQuantity +  remainingQuantity -> remainingQuantity = quantity - prevQuantity
            remainingQuantity = quantity - prevQuantity
            
            cur_profit = prices[prevQuantity] + profit[remainingQuantity]

            if cur_profit > profit[quantity]:
                profit[quantity] = cur_profit
                sequence[quantity] = prevQuantity

    return build(sequence)

def build(sequence):
    seq = []
    
    # this was the quantity consumed to fill the bottle
    idx_quantity = len(sequence) - 1
    quantityConsumed = sequence[idx_quantity]

    while idx_quantity > 0:
        seq.append(quantityConsumed)

        # x = a + b -> x - a = b
        # now out of x if a is consumed remaining is b
        idx_quantity = idx_quantity - quantityConsumed
        quantityConsumed = sequence[idx_quantity]

    return seq