"""

371. Sum of Two Integers
Medium

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

=====================================================================================================================

steps :
1] First perform XOR operation between two number.
2] Perform and operation to check if there is any carry generated.
3] If carry is generated then left shift the digit by one.
4] now repeat the steps 1 to 3 between the value obtained from step1 and value obtained from step 3 until carry = 0


Eg: 2 + 3

2   = 0 0 1 0
3   = 0 0 1 1
---------------
a^b = 0 0 0 1     ----- Step 1 this is also known as XOR
a&b = 0 0 1 0     ----- Step 2 this is also known as carry

because there is a carry

carry << 1 = 0 1 0 0      -------- Step 3

now perform xor between step 1 and step 3

0 0 0 1
0 1 0 1
---------
0 1 0 1

there is no carry return XOR
"""


class Solution():
    def getSum(self, a:int, b:int)-> int:
        xor = a ^ b
        carry = a & b

        if carry == 0:
            return xor

        return self.getSum(xor, carry << 1)


def main():
    a, b = 1, 2
    s = Solution()
    myfunc = s.getSum(a, b)
    print(myfunc)


if __name__ == '__main__':
    main()
