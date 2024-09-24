# ------------------------ Binary To Decimal ------------------------

class Solution:
    def binaryTodecimal(self, binary_str:str)->int:
        decimal_number = 0

        n = len(binary_str)

        for i in reversed(range(n)):
            cur_bit = int(binary_str[i])

            decimal_number += cur_bit * (2 ** (n-i - 1))
            # This also works
            # decimal_number += cur_bit * (1 << (n-i - 1))

        
        return decimal_number


if __name__ == '__main__':
    obj = Solution()
    
    binary_str = '1000110'
    print(obj.binaryTodecimal(binary_str=binary_str))



# ------------------------ Decimal To Binary ------------------------

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


# ------------------------ Get Set Clear Toggle ------------------------


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


# ------------------------ K-th Bit is Set or Not ------------------------

# Similar to Get Kth Bit

class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        kth_bit = n & (1 << (k))
        
        return False if kth_bit is 0 else True
    
# ------------------------ Odd or Even ------------------------

class Solution:
    def oddEven (ob,n):
        if n % 2 == 0:
            return "even"
        else:
            return "odd"

# ------------------------ Power Of Two ------------------------

'''
Tip:
    1. Numbers divisible by 2 will only have a single 1 in their binary representation.
    2. And operation between multiple of 2 and next lower number will always give 0 and other wise it will never be 0.

'''

# ------------------------ Count Set Bit ------------------------

'''
Tip:
    1. Count the number of set bit.
    2. Unset a set bit, and check how many time you un-set the bit: Kernighan’s bit count algorithm
'''


# ------------------------ Set Un-Set ------------------------

'''
One number above can set a bit
One number below can unset a bit
'''

# Set Bit 

class Solution:
	def setBit(self, n):
		return (n + 1) | n
	
#  Un-Set Bit 
class Solution:
	def unsetBit(self, n):
		return n & (n - 1)


# ------------------------ Swap Two Numbers ------------------------

class Solution:
    def get(self, a, b):
        #code here
        a , b = b , a
        return a , b
    
#   XOR 
'''
Steps:

a = a ^ b

b = a ^ b = (a ^ b) ^ b = a
ie b = a

a = a ^ b = (a ^ b) ^ b = (a ^ b) ^ a = b
ie a = b


'''
class Solution:
    def get(self, a, b):
        #code here
        a = a ^ b
        
        b = a ^ b
        
        a = a ^ b
        
        return a , b