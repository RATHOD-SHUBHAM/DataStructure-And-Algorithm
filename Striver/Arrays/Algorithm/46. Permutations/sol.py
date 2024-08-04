'''
    if there are n - numbers then there wll be n! permutations
    eg: n = 3
        3! = 6 permuations
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        visited = [False] * n

        op = []

        stack = []

        def backTrack():
            if len(stack) == n:
                op.append(stack[:])
                return
            
            # loop through every element
            for i in range(n):
                if visited[i] == True:
                    continue
                
                visited[i] = True
                stack.append(nums[i])

                # explore other elements
                backTrack()

                stack.pop()
                visited[i] = False

            return



        
        # Main Call -------
        backTrack()


        return op