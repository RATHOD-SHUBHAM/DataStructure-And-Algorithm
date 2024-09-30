'''
Prime number has only 2 factor: 1 and itself

eg: 7 = 1, 7
eg: 8
1, 8
2, 4
'''

import sys
import math
class Solution:
    def check_prime(self, num):
        count = 0
        sqrt_n = math.floor(math.sqrt(num))

        for i in range(1, sqrt_n):
            if num % i == 0:
                count += 1

                if (num // i) != i:
                    count += 1

        
        if count == 2:
            return True
        else:
            return False
        
    
if __name__ == '__main__':
    arguments = sys.argv
    ob = Solution()
    num = int(arguments[1])
    print(ob.check_prime(num=num))