class Solution:
    def countNums(self, l, r, q):
        # KEEP TRACK OF THE COUNT - WHOSE DIGIT DONT MATCH WITH PRODUCT
        countNums = 0
        for i in range(l, r + 1):
            # 10 * 2
            curProd = i * q
            # CONVERT TO SET
            prodSet = set(str(curProd))
            print(prodSet)

            # DIGIT PROD.
            # 10
            digitSet = set(str(i))
            print(digitSet)

            print(digitSet.intersection(prodSet))
            print("\n")

            if len(digitSet.intersection(prodSet)) == 0:
                countNums += 1

        return countNums



if __name__ == "__main__":
    l = 10
    r = 12
    q = 2

    obj = Solution()
    count = obj.countNums(l , r, q)
    print(count)