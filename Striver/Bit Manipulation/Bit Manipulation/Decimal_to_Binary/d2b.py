class Solution:
    def decimalTobinary(self, n:int)->int:
        binary_str = ""

        while n != 1:

            if (n%2) == 1:
                binary_str += '1'
            else:
                binary_str += '0'
            
            n = n // 2
        
        binary_str += '1' # Append the final one
        binary_str = binary_str[::-1] # reverse string

        return int(binary_str)
    
if __name__ == '__main__':
    decimal_number = 20
    obj = Solution()

    print(obj.decimalTobinary(decimal_number))