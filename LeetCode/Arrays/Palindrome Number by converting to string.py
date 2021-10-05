#todo :  this method is by converting it into a string

"""

9. Palindrome Number
Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?


"""


'''

 "This will also be taken care as reversing a single digit will still give same answer"
     if 0 <= x <= 9:
         return True

 Entire 3 step can be done in one step
     y = str(x)
     y = y[::-1]
     y = int(y)

 '''


class Solution():
    def isPalindrome(self, x: int) -> int:
        if x < 0:
            return False

        y = int(str(x)[::-1])

        if x == y:
            return True
        else:
            return False


def main():
    s = Solution()
    x = 1
    print(s.isPalindrome(x))


if __name__ == '__main__':
    main()
