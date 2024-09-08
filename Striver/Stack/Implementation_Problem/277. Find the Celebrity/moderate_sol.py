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