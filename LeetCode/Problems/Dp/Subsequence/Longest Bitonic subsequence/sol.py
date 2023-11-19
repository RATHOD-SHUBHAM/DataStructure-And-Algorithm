class Solution:
    def LongestBitonicSequence(self, nums):
        LIS_1 = self.LIS(nums)

        rev_nums = nums[:: -1]
        LIS_2 = self.LIS(rev_nums)
        LIS_2 = LIS_2[ :: -1]

        res = []
        for i in range(len(nums)):
            total = LIS_1[i] + LIS_2[i] - 1 # -1 because the peak number will be counter twice.
            res.append(total)

        return max(res)

    def LIS(self, nums):
        n = len(nums)

        dp = [1 for _ in range(n)]

        for curIdx in range(1, n):
            for prevIdx in range(curIdx):
                dontTake = 0 + dp[curIdx]
                dp[curIdx] = dontTake
                
                if nums[curIdx] > nums[prevIdx]:
                    take = 1 + dp[prevIdx]
                    dp[curIdx] = max(dp[curIdx] , take)

        return dp