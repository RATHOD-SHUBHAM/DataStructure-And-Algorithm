# todo :  https://www.youtube.com/watch?v=IOMjN6r7ju8&t=310s&ab_channel=AnishMalla

'''

To concatinate a list

    just do A + B

To Add a list elements

    Do A[i] + B[i]


'''

'''
            if A[i]!=0:
                A[i] = A[i]*A[i-1]
            else:
                A[i] = A[i]*1

            if B[i] !=0:
                B[i] = B[i]*B[i-1]
            else:
                B[i] = B[i]*1


The above statments are all single line so they can be written as

A[i] = A[i]*A[i-1] or 1

B[i] = B[i]*B[i-1] or 1


Which can further be deduced as 

A[i] *= A[i-1] or 1

B[i] *= B[i-1] or 1
'''

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = nums
        B = nums[::-1]
        print(A)
        print(B)

        # Appending from position 1 of the original string.
        # so Position Zero will remain the same we don't have to worry about that.
        for i in range(1, len(nums)):
            A[i] *= A[i - 1] or 1

            B[i] *= B[i - 1] or 1

        C = A + B
        print("\n\n")
        print(A)
        print(B)
        print(C)

        return max(C)


def main():
    s = Solution()
    nums = [2, 3, -2, 4]
    # nums = [-2,0,-1]
    # nums = [0,2]
    myfunc = s.maxProduct(nums)
    print(myfunc)


if __name__ == '__main__':
    main()
