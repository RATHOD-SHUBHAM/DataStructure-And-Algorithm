# Tc: O(n), Sc: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        maj = nums[0]

        for i in range(n):
            # if the val is same: increase count
            if nums[i] == maj:
                count += 1
            else:
                # if they are different : decrease count
                count -= 1

                # if the count becomes 0, then new element becomes majority
                if count == 0:
                    maj = nums[i]
                    count += 1
        
        return maj