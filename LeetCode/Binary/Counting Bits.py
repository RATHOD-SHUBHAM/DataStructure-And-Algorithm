"""

338. Counting Bits
Medium

Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation
and return them as an array.

"""

'''

https://www.youtube.com/watch?v=ftxesO6jdbQ&t=616s
    Even : number / 2 will have same number of ones.
    odd  : number / 2 plus 1 will have the same number of ones.
    Steps: 
        1] Divide the number by 2.
        2] perform and operation in between number and one.
        this step adds one if it is a odd number else it will add zero if it is a even number.
        3] add step 1 and step 2

'''
from typing import List


class Solution():
    def countBits(self, num:int) -> List[int]:
        # todo : always remember 'int' has no len()
        result = [0]
        for i in range(1,num+1):
            print(i)
            # print( i>>1)
            print(result)
            result.append(result[i >> 1] + int(i & 1))
            print("result after append: ",result)
        return result


def main():
    num = 2
    s = Solution()
    print(s.countBits(num))


if __name__ == '__main__':
    main()