from collections import Counter
class Solution:
    def twoOddNum(self, Arr, N):
        counter = Counter(Arr)
        
        odd_num = []
        for item, count in counter.items():
            if count % 2 == 1:
                odd_num.append(item)
        
        odd_num = sorted(odd_num)
        return odd_num[::-1]
    

# -------------------------------------------------

'''
1. Xor of all numbers
2. Extract the right most bit mast
3. Get the 2 number from the bit
'''

class Solution:
    def twoOddNum(self, Arr, N):
        # 1. XOR of numbers
        xor = 0
        for i in range(N):
            xor ^= Arr[i]
        
        # Extrct the right most bit mast
        right_bit_mask = xor & (~(xor - 1))
        
        # Get the Two numbers
        x = y = 0
        for i in range(N):
            if Arr[i] & right_bit_mask == 0:
                x ^= Arr[i]
            else:
                y ^= Arr[i]
        
        op = []
        if x <= y:
            op.append(y)
            op.append(x)
        else:
            op.append(x)
            op.append(y)
    
        return op