'''
Generating Rules:
    Roman Numerals are made with 7 single-letter symbols, each with its own value. A
    dditionally, the subtractive rules  give an additional 6 symbols. 
    
    This gives us a total of 13 unique symbols (each symbol is made of either 1 letter or 2).


    Secondly, Roman Numericals are writtern from Largest to smallest
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        rules = [
            ("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10),("XL", 40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)
            ]

        
        roman_number = ""
        # Roman number are from largest to smallest
        for symbol, value in reversed(rules):

            count = num // value # count of symbol

            if count == 0:
                '''
                    Larger number dividing smaller number.
                '''
                continue

            num = num % value # get the remainder

            # get the amount of symbol needed
            sym = symbol * count # multiply str and int


            roman_number += sym
        
        return roman_number



            
