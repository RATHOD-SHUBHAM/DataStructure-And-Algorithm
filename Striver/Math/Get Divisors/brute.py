'''
36

1 x 36
2 x 18
3 x 12
4 x 9
6 x 6
9 x 4
12 x 3
18 x 2
36 x 1

'''

class Solution:
    def sumOfDivisors(self, N):
        factors = 0
        for i in range(1, N+1):
            if (N % i) == 0:
                factors += i
        return factors