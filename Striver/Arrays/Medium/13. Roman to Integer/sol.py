'''
Generating Rules:
    Roman Numerals are made with 7 single-letter symbols, each with its own value. A
    dditionally, the subtractive rules  give an additional 6 symbols. 
    
    This gives us a total of 13 unique symbols (each symbol is made of either 1 letter or 2).


    Secondly, Roman Numericals are writtern from Largest to smallest
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        rules = {
            "I": 1,
            "IV": 4, 
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        i = 0

        integer_val = 0

        while i < len(s):
            # check if 2 char are present
            if s[i : i+2] in rules:
                integer_val += rules[s[i : i+2]]
                i += 2
            else:
                integer_val += rules[s[i]]
                i += 1

        return integer_val