# Tc: O(n ^ 2) | Sc: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        difference = math.inf
        op = 0

        for i in range(n):

            left = i + 1 
            right = n - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                
                # Find out if the cur sum is closest to target
                cur_diff = abs(target - cur_sum)
                if cur_diff < difference:
                    difference = cur_diff
                    op = cur_sum
                
                # Goal is to move closer to the target
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1

        return op 