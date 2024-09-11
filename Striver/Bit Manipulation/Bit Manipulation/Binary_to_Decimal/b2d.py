class Solution:
    def binaryTodecimal(self, binary_str:str)->int:
        decimal_number = 0

        n = len(binary_str)

        for i in reversed(range(n)):
            cur_bit = int(binary_str[i])

            decimal_number += cur_bit * (2 ** i)
        
        return decimal_number


if __name__ == '__main__':
    obj = Solution()
    
    binary_str = '1011'
    print(obj.binaryTodecimal(binary_str=binary_str))
