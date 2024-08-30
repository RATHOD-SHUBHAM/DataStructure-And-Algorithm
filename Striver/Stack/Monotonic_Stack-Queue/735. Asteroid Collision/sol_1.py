# Tc: O(n) | Sc: O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)

        stack = []

        for i in range(n):
            cur_ele = asteroids[i]

            if cur_ele > 0:
                stack.append(cur_ele)
            else:
                # Cur value is greater
                while stack and stack[-1] > 0 and abs(cur_ele) > stack[-1]:
                    stack.pop()
            
                if stack and abs(cur_ele) == stack[-1]:
                    stack.pop()

                elif not stack or stack[-1] < 0:
                    stack.append(cur_ele)

        return stack