'''
The definition of a celebrity is that: 
All the other n - 1 people know the celebrity, 
but the celebrity does not know any of them.

Celebrity:
Known by = n - 1
Knows = 0
'''

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        graph = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if knows(i , j):
                    graph[i][j] = 1
        
        # print(graph)

        known_by = [0] * n
        for col in range(n):
            for row in range(n):
                if row == col:
                    continue
                
                if graph[row][col] == 1:
                    known_by[col] += 1

        _knows = [0] * n
        for row in range(n):
            for col in range(n):
                if row == col:
                    continue
                
                if graph[row][col] == 1:
                    _knows[row] += 1
        
        # print(known_by)
        # print(_knows)

        for i in range(n):
            if known_by[i] == n - 1 and _knows[i] == 0:
                return i
        
        return -1