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