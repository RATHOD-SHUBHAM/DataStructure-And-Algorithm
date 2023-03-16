#!/bin/python3

import math
import os
import random
import re
import sys


def hourGlassSum(row, col, arr):
    # start from the center
    hourGlass_sum = 0
    hourGlass_sum += arr[row - 1][col - 1] + arr[row - 1][col] + arr[row - 1][col + 1]
    hourGlass_sum += arr[row][col]
    hourGlass_sum += arr[row + 1][col - 1] + arr[row + 1][col] + arr[row + 1][col + 1]
    return hourGlass_sum


if __name__ == '__main__':
    arr = []
    maximum_hour_glass = -999

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    """
            # start from 2
            1  2  3
            4  5  6       # start from 5
            7  8  9
    
    If i start from center i can cover every six corner.
    """
    for row in range(1, 5):
        for col in range(1, 5):
            hourGlass = hourGlassSum(row, col, arr)
            if maximum_hour_glass < hourGlass:
                maximum_hour_glass = hourGlass

    print(maximum_hour_glass)