import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.myStack = []  # First In Last Out
        self.myQueue = list()  # First In First Out

    def pushCharacter(self, char):
        self.myStack.append(char)

    def enqueueCharacter(self, char):
        self.myQueue.append(char)

    def popCharacter(self):
        # pop() or pop(-1) or popright() removes the last element from the list
        return (self.myStack.pop())

    def dequeueCharacter(self):
        # pop(0) or popleft() returns the first element from the list
        return (self.myQueue.pop(0))


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")    