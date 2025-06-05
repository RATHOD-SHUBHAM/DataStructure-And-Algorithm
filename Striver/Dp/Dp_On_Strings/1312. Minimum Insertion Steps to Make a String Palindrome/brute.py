"""
Idea is to find non paired value, and return its count

But this wont work
For eg: "leetcode"
it will return 6

because it doesnt consider that eee can form a palindrome itself

But this gives a idea thatwe can use paired values
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        counter = collections.Counter(s)

        odd_count = 0
        for _, count in counter.items():
            if count % 2 != 0:
                odd_count += 1

        if len(s) % 2 != 0:
            return odd_count - 1
        else:
            return odd_count
        