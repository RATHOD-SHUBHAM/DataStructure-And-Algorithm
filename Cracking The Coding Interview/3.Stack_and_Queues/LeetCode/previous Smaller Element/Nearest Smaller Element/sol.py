class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = []
        g = [-1] * len(A)

        for i in range(len(A)):
            while stack and stack[-1] >= A[i]:
                stack.pop()
                
            if stack:
                g[i] = stack[-1]

            stack.append(A[i])
            
        return g

if __name__ == '__main__':
    sol = Solution()
    # ip = [4, 5, 2, 10, 8]
    ip = [3, 2, 1]
    pse = sol.prevSmaller(ip)
    print(pse)