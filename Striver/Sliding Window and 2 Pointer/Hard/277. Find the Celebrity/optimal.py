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