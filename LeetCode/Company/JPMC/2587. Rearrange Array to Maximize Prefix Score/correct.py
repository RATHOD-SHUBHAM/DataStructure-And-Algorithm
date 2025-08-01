# The score of nums is the number of positive integers in the array prefix
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        # bring all positive in front to increase the score
        sorted_num = sorted(nums, reverse = True)
        # print(sorted_num)

        prefix_sum = score = 0

        for i in range(n):
            prefix_sum += sorted_num[i]

            if prefix_sum > 0:
                score += 1
            else:
                # the prefix sum will only decrease because we have sorted the array
                return score      
        
        return score