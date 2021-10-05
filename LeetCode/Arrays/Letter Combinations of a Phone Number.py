"""

17. Letter Combinations of a Phone Number.

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters


"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        combination = []

        def recur(rest_of_the_digit, path_so_far):
            print("rest of the digit is: ", rest_of_the_digit)
            print("path so far: ", path_so_far)

            # if there are no more digit.
            if not rest_of_the_digit:
                combination.append(path_so_far)
                return

            first_digit = rest_of_the_digit[0]
            print("the first digit is: ", first_digit)
            remaining_digit = rest_of_the_digit[1:]
            print("the remaining digit: ", remaining_digit)

            letters = phone[first_digit]
            print(letters)

            for letter in letters:
                print(letter)
                recur(remaining_digit, path_so_far + letter)
                print("\n")

        recur(digits, "")

        return combination