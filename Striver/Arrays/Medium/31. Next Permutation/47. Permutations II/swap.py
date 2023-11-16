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