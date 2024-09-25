# --------------------- Brute Force ---------------------

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives
        # for the reasons explained above.
        # Also, we count the number of negatives signs.
        negatives = False
        if dividend < 0 and divisor >= 0:
            negatives = True
        if divisor < 0 and dividend >= 0:
            negatives = True

        # Count how many times the divisor has to be
        # added to get the dividend. This is the quotient.
        quotient = 0
        while dividend - divisor >= 0:
            quotient += 1
            dividend -= divisor

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives == True else quotient
    


# --------------------- Power of 2 ---------------------


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives
        # for the reasons explained above.
        # Also, we count the number of negatives signs.
        negatives = True
        if dividend < 0 and divisor >= 0:
            negatives = False
        if divisor < 0 and dividend >= 0:
            negatives = False

        # Count how many times the divisor has to be
        # added to get the dividend. This is the quotient.
        quotient = 0
        n = abs(dividend)
        d = abs(divisor)
        while n >= d:
            count = 0

            while n >= (d * (2 ** count)):
                count += 1
            
            count = count - 1

            quotient += 2 ** count

            n = n - (d * (2 ** count))

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != True else quotient
    
# --------------------- bit Manipulation ---------------------
# Change 2 ** x -> 1 << x
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = (2 ** 31) - 1 # 2147483647  # 2**31 - 1
        MIN_INT = -(2 ** 31) # -2147483648  # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives
        # for the reasons explained above.
        # Also, we count the number of negatives signs.
        negatives = True
        if dividend < 0 and divisor >= 0:
            negatives = False
        if divisor < 0 and dividend >= 0:
            negatives = False

        # Count how many times the divisor has to be
        # added to get the dividend. This is the quotient.
        quotient = 0
        n = abs(dividend)
        d = abs(divisor)
        while n >= d:
            count = 0

            while n >= (d * (1 << count)):
                count += 1
            
            count = count - 1

            quotient += 1 << count

            n = n - (d * (1 << count))

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != True else quotient
    



# --------------------- Alternate Power of 2 ---------------------

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