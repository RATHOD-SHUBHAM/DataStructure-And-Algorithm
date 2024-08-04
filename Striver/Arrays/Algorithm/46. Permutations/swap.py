'''
    if there are n - numbers then there wll be n! permutations
    eg: n = 3
        3! = 6 permuations
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)


        op = []

        def backTrack(i):
            if i == n:
                op.append(nums[:])
                return
            
            # loop through every element
            for j in range(i, n):
                # swap element
                nums[i] , nums[j] = nums[j] , nums[i]

                backTrack(i + 1)

                # Swap the elements back
                nums[i] , nums[j] = nums[j] , nums[i]


        # Main Call -------
        
        backTrack(0)


        return op