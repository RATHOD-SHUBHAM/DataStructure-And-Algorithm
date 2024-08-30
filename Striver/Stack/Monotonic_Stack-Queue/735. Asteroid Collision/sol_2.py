'''
The else clause is only executed when your while condition becomes false. 
If you break out of the loop, or if an exception is raised, it won't be executed.
'''

# Tc: O(n) | Sc: O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)

        stack = []

        for i in range(n):
            cur_ele = asteroids[i]

            # if collision
            while stack and (cur_ele < 0 and stack[-1] > 0):
                # stack value is greater
                if abs(stack[-1]) > abs(cur_ele):
                    break
                
                # Both are same and will explode
                elif abs(stack[-1]) == abs(cur_ele):
                    stack.pop()
                    break
                
                else:
                    # Cur value is greater
                    stack.pop()
            
            # If the while loop breaks, the else statement is not executed
            else:
                stack.append(cur_ele)
        
        return stack