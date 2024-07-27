class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        idx = 0

        # Step 1: Whitespaces
        while idx < n and s[idx] == ' ':
            idx += 1
        
        # Step 2: Signedness
        sign = 1
        if idx < n and s[idx] == '-':
            sign = -1
            idx += 1
        elif idx < n and s[idx] == '+':
            sign = 1
            idx += 1

        INT_MAX = (2 ** 31) - 1
        INT_MAX_PREV = INT_MAX // 10

        INT_MIN = -(2 ** 31)
        INT_MIN_PREV = INT_MIN // 10
        
        number = 0

        while idx < n and s[idx].isdigit():
            # Step 3: Conversion
            digit = int(s[idx])

            # Step 4: Rounding
            if number > INT_MAX_PREV or (number == INT_MAX_PREV and digit > 7):
                return INT_MIN if sign == -1 else INT_MAX
            elif number < INT_MIN_PREV or (number == INT_MIN_PREV and digit > 8):
                return INT_MIN
            
            number = (number * 10) + digit 
            idx += 1
        
        return number * sign

