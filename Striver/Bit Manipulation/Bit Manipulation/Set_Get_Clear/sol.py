class Solution:
    def bitManipulation(self, num, i):
        print('num: ', num)
        
        # 1. Get the i-th bit
        ith_bit = (num >> (i - 1)) & 1
        print('Get: ', ith_bit)
        
        # 2. Set the i-th bit
        set_num = num | (1 << (i - 1))
        print("set bit: ", set_num)
        
        # 3. Clear the i-th bit
        clear_num = num & ~(1 << (i - 1))
        
        # 4. Toggle the i-th bit
        toggle = num ^ (1 << (i - 1))
        print(toggle)
        
        # Print the results as space-separated values
        print(ith_bit, set_num, clear_num)


if __name__ == '__main__':
    obj = Solution()

    num = 70
    i = 3

    obj.bitManipulation(num=num, i = i)