class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        return a
        
        '''

        # Prevents overflow in python
        mask = 0xffffffff # bitmask of 32 1-bits.

        while (mask & b) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        return (mask & a) if b > 0 else a

