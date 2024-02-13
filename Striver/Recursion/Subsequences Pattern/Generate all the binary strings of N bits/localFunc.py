class Solution:
    def __init__(self) -> None:
        self.result = []

    def generateAllBinaryStrings(self, n):
        # base case
        if n == 0:
            return self.result
        
        if n == 1:
            return ['0' , '1']

        # function call
        st = []
        self.dfs(st, n)

        return self.result

    def dfs(self, st , n):
        # base case
        if n == 0:
            val = ''.join(st)
            self.result.append(val)
            return
        
        # Attach 0
        st.append("0")
        self.dfs(st, n - 1)
        st.pop()

        # Attach 1
        st.append("1")
        self.dfs(st, n - 1)
        st.pop()

        return
    


if __name__ == '__main__':
    obj = Solution()
    print(obj.generateAllBinaryStrings(3))