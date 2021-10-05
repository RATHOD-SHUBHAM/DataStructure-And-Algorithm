# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

T = int(input())


# If a number is divisible by another number less than or equal to the square root of the number...
# then it is NOT prime
def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i is 0:
            return False
    return True


for _ in range(T):
    n = int(input())

    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")
