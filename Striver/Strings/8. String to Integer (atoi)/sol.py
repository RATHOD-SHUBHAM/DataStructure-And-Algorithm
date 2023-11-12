'''
    Follow the 4 rules:
        1. Remove any white spaces.
        2. get the sign of number.
        3. Convert integer to string.
        4. Check if the number is with in the range (-2^31 to 2^31 - 1)
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        sign = 1 # positive
        number = 0
        idx = 0

        INT_MAX = (2 ** 31) - 1
        INT_MIN = -(2 ** 31)

        print(INT_MAX, INT_MIN)

        # Rule 1: Remvoe white spaces
        while idx < n and s[idx] == " ":
            idx += 1
        
        # Rule 2: Get the sign of next character
        if idx < n and s[idx] == "+":
            sign = 1
            idx += 1
        elif idx < n and s[idx] == '-':
            sign = -1
            idx += 1
        
        # Rule 3: Convert string to Integer
        while idx < n and s[idx].isdigit():
            digit = int(s[idx]) # convert to integer

            # print("number: ",number)
            # print("digit: ",digit)
            # print("int_max / 10: ", INT_MAX // 10)
            # print("INT_MIN / 10: ", INT_MIN // 10)
            # INT_MAX // 10:  214748364
            # INT_MIN // 10:  -214748365
            # print("\n")

            # # Rule 4: Check for Underflow or Overflow
            if (number > INT_MAX // 10) or (number == INT_MAX // 10 and digit > 7) :
                # if the number is negative - we need to return underflow value
                return INT_MAX if sign == 1 else INT_MIN
            
            if (number < INT_MIN // 10 ) or (number == INT_MIN // 10 and digit > 8):
                return INT_MIN

            # append the current digit to number
            number = number * 10 + digit
            idx += 1
        
        # We have formed a valid number without any overflow/underflow.
        number =  sign * number

        return number
        

