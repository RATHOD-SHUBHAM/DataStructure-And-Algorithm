# todo: this method is done without converting to string

"""

9. Palindrome Number
Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?


"""


'''

    Step 1 : divide the number by 10 and take the reminder
    step 2: multiply that reminder with 10 each time a new number is being added
    step 3: take the quosient and repeat the entire proces still there is no element or zero left in the quoesient

'''
class Solution():
    def isPalindrome(self, x: int) -> int:
        if x < 0: return False
        else:
            reverse_x = x
            # print(reverse_x)
            rev = 0
            while reverse_x > 0:
                reminder = reverse_x % 10
                # print(reminder)
                rev = rev * 10 + reminder
                # print(rev)
                reverse_x = reverse_x // 10
            # print(rev)
            if rev == x:
                return True
            else:
                return False


def main():
    s = Solution()
    x = 1
    print(s.isPalindrome(x))


if __name__ == '__main__':
    main()
