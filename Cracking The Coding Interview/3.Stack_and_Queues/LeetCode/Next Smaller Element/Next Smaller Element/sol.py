from tkinter import N


class Solution:
    def NSE(self, array):
        n = len(array)
        stack = []
        nse = [-1] * n
        
        for i in reversed(range(n)):
            while stack and stack[-1] >= array[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]
            else:
                nse[i] = -1

            stack.append(array[i])

        return nse



if __name__ == '__main__':
    ip = [4, 8, 5, 2, 25]
    sol = Solution()
    nse = sol.NSE(ip)
    print(nse)