"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""
"""
Steps: 
1] find the smallest element in the list of string
2] compare each element of the first string with every element of other string.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if the string is null return "" if string has just 1 element return that element
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        # find the smallest string
        minValue = len(strs[0])
        for i in range(1, len(strs)):
            minValue = min(minValue, len(strs[i]))
            # print(minValue)
            # 4
        output = ""
        i = 0
        while i < minValue:
            CompChar = strs[0][i]
            for x in range(1, len(strs)):
                if strs[x][i] != CompChar:
                    return output
            output = output + CompChar
            i += 1
        return output