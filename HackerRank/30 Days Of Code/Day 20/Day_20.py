#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
# print(a)

swaps = 0

for j in range(n - 1):
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            swaps += 1
            a[i + 1], a[i] = a[i], a[i + 1]

print("Array is sorted in {} swaps.".format(swaps))
print("First Element:", a[0])
print("Last Element:", a[-1])
