# Tc: O(n)
# Sc: O(1) if we are considering we only take two value

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash_counter = {}
        cash_counter[5] = 0
        cash_counter[10] = 0

        # Iterate through each bill
        for cash in bills:
            if cash == 5:
                # I dont have to return anything
                cash_counter[5] += 1
            elif cash == 10:
                if cash_counter[5] > 0:
                    cash_counter[5] -= 1
                    cash_counter[10] += 1
                else:
                    return False
            elif cash == 20:
                if cash_counter[10] > 0 and cash_counter[5] > 0:
                    cash_counter[10] -= 1
                    cash_counter[5] -= 1
                elif cash_counter[5] >= 3:
                    cash_counter[5] -= 3
                else:
                    return False
        
        return True
    
# ------------------------- Same Solution but with different variable names -------------------------

# Tc: O(n)
# Sc: O(1)

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = 0
        ten_dollar = 0

        # Iterate through each bill
        for cash in bills:
            if cash == 5:
                # I dont have to return anything
                five_dollar += 1
            elif cash == 10:
                if five_dollar > 0:
                    five_dollar -= 1
                    ten_dollar += 1
                else:
                    return False
            elif cash == 20:
                if ten_dollar > 0 and five_dollar > 0:
                    ten_dollar -= 1
                    five_dollar -= 1
                elif five_dollar >= 3:
                    five_dollar -= 3
                else:
                    return False
        
        return True