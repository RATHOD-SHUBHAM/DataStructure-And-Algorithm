"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.



"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # creating a array of the same size as my input string and initializing them with 0
        # eg: input = "1234"
        # array = | 1 | 2 | 3 | 4 |
        #         | 0 | 0 | 0 | 0 |
        DecodeArray = [0 for i in range(n)]

        # if my first element of the string is not Zero then I change the value of first element of Decode array to 1
        if s[0] != '0':
            DecodeArray[0] = 1

        # starting from the first Index
        for i in range(1, n):
            # single digit eg "1"
            x = int(s[i])
            # double digit eg "12"
            y = int(s[i - 1: i + 1])

            # single sigit should be between 1-9
            if x >= 1 and x <= 9:
                # add the previous element
                DecodeArray[i] += DecodeArray[i - 1]
            # for double digit
            if y >= 10 and y <= 26:
                if i - 2 >= 0:
                    # add previous of previous element if index is greater than one
                    DecodeArray[i] += DecodeArray[i - 2]
                else:
                    # just add one if index is 1
                    DecodeArray[i] += 1

        # return the last element
        return DecodeArray[-1]
