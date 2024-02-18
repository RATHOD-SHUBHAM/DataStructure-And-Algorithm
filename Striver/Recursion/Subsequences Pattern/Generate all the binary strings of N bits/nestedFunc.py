# Solution 1
class Solution:
    def __init__(self) -> None:
        self.result = []

    def generateAllBinaryStrings(self, n):
        # base case
        if n == 0:
            return self.result
        
        if n == 1:
            return ['0' , '1']

        def dfs(st , n):
            # base case
            if n == 0:
                val = ''.join(st)
                self.result.append(val)
                return
            
            # Attach 0
            st.append("0")
            dfs(st, n - 1)
            st.pop()

            # Attach 1
            st.append("1")
            dfs(st, n - 1)
            st.pop()

            return




        # function call
        st = []
        dfs(st, n)

        return self.result
    


if __name__ == '__main__':
    obj = Solution()
    print(obj.generateAllBinaryStrings(3))