class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (2 ** 31) - 1
        INT_MIN = -(2 ** 31)

        # Check for Negative
        negative = False
        if dividend < 0 and divisor >= 0:
            negative = True
        if divisor < 0 and dividend >= 0:
            negative = True
        

        # Main Logic
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            count = 0

            while dividend >= (divisor * (2 ** count)):
                count += 1
            
            count -= 1
            quotient += 2 ** count
            dividend -= divisor * (2 ** count)

        
        # Return Conditions
        if negative == True:
            quotient *= -1

        if quotient > INT_MAX:
            return INT_MAX
        elif quotient< INT_MIN:
            return INT_MIN
        else:
            return quotient