'''
    numerator = (A + nx)
    denominator = (m + n)

    numerator.   [3,2,4,3] + 2x
    ---------  = ------------   = 4 (mean)
    denominator  4 + 2 = (6)

    [3,2,4,3] + 2x = 6 * 4 (mean * denominator)

    12 + 2x = 24 

    2x = 24 - 12 (mean * denominator) - A

    2x = 12 

    x = 6 (mean * denominator) - A // n
'''

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        A = sum(rolls)
        m = len(rolls)

        x = ((mean * (m + n)) - A)

        dice_val = x // n # value for each dice

        # A dice can have value only between 1 - 6
        if dice_val > 6 or dice_val < 1:
            return []

        # Distribute the dice value among n dice
        op = [dice_val] * n

        # Remaining value that needs to be distribute among dice
        distribute_val = x % n 

        if dice_val == 6 and distribute_val > 0:
            return []

        # if there is a value to distribute
        for i in range(distribute_val):
            op[i] += 1
        
        return op
        

