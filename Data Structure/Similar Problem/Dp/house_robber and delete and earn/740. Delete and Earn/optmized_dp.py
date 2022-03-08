# https://www.youtube.com/watch?v=7FCemBxvGw0&ab_channel=NeetCode
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        # print(count)
        
        nums = list(set(nums))
        
        nums.sort()
        
        # print(nums)
        
        
        prev_earning = 0
        before_prev_earning = 0
        
        for i in range(len(nums)):
            cur_earning = nums[i] * count[nums[i]]
            # print("cur_earning: ",cur_earning)

            if i > 0 and nums[i] == nums[i-1] + 1:
                # because we have sorted prev val + 1 = cur_val
                earning = max(cur_earning + before_prev_earning, prev_earning)
                # before_prev_earning = prev_earning
                # prev_earning = earning
            else:
                # cur_earning + what ever i earned so far
                earning = cur_earning + prev_earning
                # before_prev_earning = prev_earning
                # prprev_earningev = earning
            before_prev_earning = prev_earning
            prev_earning = earning
            
        return prev_earning
            
        