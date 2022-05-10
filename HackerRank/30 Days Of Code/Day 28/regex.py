#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    name = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        #  list of people whose email address ends in @gmail.com

        if "@gmail.com" in emailID:
            name.append(firstName)

    name.sort()
    for i in name:
        print(i)

