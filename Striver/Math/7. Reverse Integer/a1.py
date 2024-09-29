# ------------------------  Brute Stack  ------------------------

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)

        is_negative = False
        if x < 0:
            is_negative = True
        
        x = abs(x)
        str_x = str(x)

        st = []

        for i in range(len(str_x)):
            st.append(str_x[i])

        new_num = ""
        while st:
            new_num += st.pop()
        
        reversed_number = int(new_num)
        
        if is_negative == True:
            reversed_number *= -1
        
        if reversed_number < INT_MIN or reversed_number > INT_MAX:
            return 0
        else:
            return reversed_number
        
    
# ------------------------  Math  ------------------------


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)

        is_negative = False
        if x < 0:
            is_negative = True
        
        x = abs(x)

        reversed_number = 0
        while x > 0:
            remainder = x % 10
            reversed_number = reversed_number * 10 + remainder
            x = x // 10
        
        if is_negative == True:
            reversed_number *= -1
        
        if reversed_number < INT_MIN or reversed_number > INT_MAX:
            return 0
        else:
            return reversed_number