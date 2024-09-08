'''
The definition of a celebrity is that: 
All the other n - 1 people know the celebrity, 
but the celebrity does not know any of them.

Celebrity:
Known by = n - 1
Knows = 0
'''

# ---------------------- Brute Force ----------------------

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
    


# ---------------------- Better Brute Force ----------------------

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
        _knows = [0] * n
        for row in range(n):
            for col in range(n):
                if row == col:
                    continue
                
                if graph[row][col] == 1:
                    _knows[row] += 1
                    known_by[col] += 1
        
        # print(known_by)
        # print(_knows)

        for i in range(n):
            if known_by[i] == n - 1 and _knows[i] == 0:
                return i
        
        return -1
    

# ---------------------- Moderate  Solution ----------------------


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

        # Eliminate Non Celebirty People
        top = 0
        bottom = n - 1

        while top < bottom:
            if graph[top][bottom] == 1:
                top += 1
            elif graph[bottom][top] == 1:
                bottom -= 1
            else:
                '''
                    Some has to know the other, because celrity is know by n - 1 people
                '''
                top += 1
                bottom -= 1
        
        if top > bottom:
            return - 1
        else:
            # Verify if he is the celebrity
            for i in range(n):
                if top == i:
                    continue
                
                if graph[top][i] != 0 or graph[i][top] != 1:
                    return -1
        
            return top
        

# ---------------------- Optimal  Solution ----------------------

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:


        # Eliminate Non Celebirty People
        top = 0
        bottom = n - 1

        while top < bottom:
            if knows(top, bottom) == True:
                top += 1
            elif knows(bottom, top) == True:
                bottom -= 1
            else:
                '''
                    Some has to know the other, because celrity is know by n - 1 people
                '''
                top += 1
                bottom -= 1
        
        if top > bottom:
            return - 1
        else:
            # Verify if he is the celebrity
            for i in range(n):
                if top == i:
                    continue
                
                if knows(top, i) == True or knows(i, top) == False:
                    return -1
        
            return top