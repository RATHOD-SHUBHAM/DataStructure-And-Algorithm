'''
    start
    t m m z u x t
    i

    When i encounter m for the second time, so will have to  start from my counting again from there.

    and if my start pointer has crossed a duplicate value. for eg t.
    My start pointer would be at m = 2 and it will again encounter a 't' in the end.
    but rather than incrementing my start pointer there i will increase my count because it is not a duplicate value in mzuxt.
    start <= dict[s[i]] --> this condition satisfies the above case

    i-start+1 = this is to make sure i dont count the repeating characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, count = 0, 0
        dict = {}

        for i in range(len(s)):
            if s[i] in dict and start <= dict[s[i]]:
                start = dict[s[i]] + 1
            else:
                count = max(count, i - start + 1)
            dict[s[i]] = i
        return count


def main():
    s = "tmmzuxt"
    st = Solution()
    myfunc = st.lengthOfLongestSubstring(s)
    print(myfunc)


if __name__ == '__main__':
    main()