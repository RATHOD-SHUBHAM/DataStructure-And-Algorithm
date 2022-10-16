# Tc and Sc = O(n)

class Solution:
    def PGE(self, array):
        stack = []
        n = len(array)
        pge = [-1] * n

        for i in range(n):
            while stack and stack[-1] <= array[i]:
                stack.pop()

            if stack:
                pge[i] = stack[-1]
            else:
                pge[i] = -1

            stack.append(array[i])

        
        return pge

    
if __name__ == '__main__':
    sol = Solution()
    ip = [10, 4, 2, 20, 40, 12, 30]
    pge = sol.PGE(ip)
    print(pge)
