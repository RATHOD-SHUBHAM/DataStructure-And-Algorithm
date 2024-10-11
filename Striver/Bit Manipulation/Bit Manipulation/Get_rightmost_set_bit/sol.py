class Solution:
    def get_rightmost_set_bit(self, n):
        # Turn of the right most bit
        val = n & (n - 1)

        # Get th bit that was turned off
        right_most_set_bit = val ^ n

        return right_most_set_bit
    
    def get_rightmost_set_bit_sinlge_line(self, n):
        '''
        Single line code
        '''
        return (n & (n-1)) ^ n


if __name__ == '__main__':
    obj = Solution()

    n = 14
    right_most_set_bit = obj.get_rightmost_set_bit(n)

    print(right_most_set_bit)

    right_most_set_bit_single_line = obj.get_rightmost_set_bit_sinlge_line(n)
    print(right_most_set_bit_single_line)