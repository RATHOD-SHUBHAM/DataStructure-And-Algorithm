# https://www.youtube.com/watch?v=7FCemBxvGw0&ab_channel=NeetCode
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        # print(count)
        
        nums = list(set(nums))
        
        nums.sort()
        
        # print(nums)
        
        
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            cur_earning = nums[i] * count[nums[i]]
            # print("cur_earning: ",cur_earning)
            
            if i == 0:
                dp[i] = cur_earning
            else:
                if nums[i] == nums[i-1] + 1: # because we have sorted prev val + 1 = cur_val
                    dp[i] = max(cur_earning+dp[i-2], dp[i-1])
                else:
                    # cur_earning + what ever i earned so far
                    dp[i] = cur_earning + dp[i-1]
        return dp[-1]
            
        