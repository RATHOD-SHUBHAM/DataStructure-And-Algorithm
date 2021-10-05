'''

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.




'''

class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1: return 1
        maxcount = 0
        count = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                # print(s[i])
                count += 1
                # print(count)
            else:
                count = 1
                print("am here")
            maxcount = max(maxcount,count)

        return maxcount


def main():
    # s = "abbcccddddeeeeedcba"
    # s = "leeeetcodee"
    s = "jk"
    sol = Solution()
    myfunc = sol.maxPower(s)
    print(myfunc)


if __name__ == '__main__':
    main()
