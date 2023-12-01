class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        sign = 1
        idx = 0

        INT_MAX = (2 ** 31) - 1
        INT_MIN = - (2 ** 31)

        print(INT_MAX , INT_MIN) # 2147483647 -2147483648
        print(INT_MAX // 10, INT_MIN // 10) # 214748364 -214748364

        number = 0

        # 1. Remove white spaces
        while idx < n and s[idx] == " ":
            idx += 1

        # 2. Check for sign
        if idx < n and s[idx] == "+":
            sign = 1
            idx += 1
        elif idx < n and s[idx] == "-":
            sign = -1
            idx += 1

        
        # 3. Convert string to Integer
        while idx < n and s[idx].isdigit():
            digit = int(s[idx])

            # Check for over flow and under flow
            if (number > INT_MAX // 10) or (number == INT_MAX // 10 and digit > 7) :
                return INT_MAX if sign == 1 else INT_MIN
            
            if (number < INT_MIN // 10) or (number == INT_MIN // 10 and digit > 8):
                return INT_MIN
            
            # append digit to number
            number = number * 10 + digit

            idx += 1
    
        number = sign * number

        return number