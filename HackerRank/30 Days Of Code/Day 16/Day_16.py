#!/bin/python3

import sys


S = input().strip()
print(type(S))

try:
    # expecting a integer value. If it doesnot get a decimal value it will throw an error
    ip = int(S)
    print(ip)
except:
    print("Bad String")