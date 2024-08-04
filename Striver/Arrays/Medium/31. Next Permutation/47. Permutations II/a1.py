# --------------------------  Recursion --------------------------

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        visited = [False] * n

        op = []

        stack = []

        def backTrack():
            if len(stack) == n:
                if stack[:] not in op:
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
    


# --------------------------  Swapping --------------------------

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        op = []

        # helper ----
        def backTrack(i):
            if i == n:
                if nums not in op:
                    op.append(nums[:])
                return
            
            for j in range(i , n):
                nums[i] , nums[j] = nums[j] , nums[i]

                backTrack(i + 1)

                nums[i] , nums[j] = nums[j] , nums[i]


        # main ---
        backTrack(0)

        return op