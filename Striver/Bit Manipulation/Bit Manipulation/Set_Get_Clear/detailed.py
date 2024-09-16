class Solution:
    def get_ith_bit(self, num, i):
        '''
        Move the ith bit to the end
        Perform AND -> 1 & 1 = 1
        return the value
        '''

        ith_bit = (num >> (i - 1)) & 1
        print("Get ith bit: ", ith_bit)
    
    def set_ith_bit(self, num, i):
        '''
        Set = Make the bit 1

        OR operation will help set the bit
        Move the 1 to the ith position

        0 | 1 = 1
        '''

        set_num = num | (1 << (i - 1))
        print('Set value: ', set_num)
    
    def clear_bit(self, num, i):
        '''
        Clear = Make the bit 0

        Have a 0 at the it bit and remaining as 1,
        Performing AND operation will keep all the bit the same, except the ith bit

        0 & 0 = 0
        0 & 1 = 0
        1 & 0 = 0
        1 & 1 = 1
        '''
        negate_ith_bit = ~(1 << (i - 1))
        clear_ith_bit = num & negate_ith_bit

        print("Clear bit: ", clear_ith_bit)
    
    def toggle_bit(self, num, i):
        '''
        Toggle: Flip 0 to 1 or 1 to 0

        XOR operator does that

        0 ^ 0 = 0
        0 ^ 1 = 1
        1 ^ 0 = 1
        1 ^ 1 = 0
        '''

        toggle_bit = num ^ (1 << (i-1))
        print('Toggle Bit: ', toggle_bit)


    def bitManipulation(self, num, i):
        print('num: ', num)
        
        # 1. Get the i-th bit
        self.get_ith_bit(num, i)
        
        # 2. Set the i-th bit
        self.set_ith_bit(num, i)
        
        # 3. Clear the i-th bit
        self.clear_bit(num, i)
        
        # 4. Toggle the i-th bit
        self.toggle_bit(num, i)


if __name__ == '__main__':
    obj = Solution()

    num = 70
    i = 3

    obj.bitManipulation(num=num, i = i)