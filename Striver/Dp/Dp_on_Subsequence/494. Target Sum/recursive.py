class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        """
        We know , 
        we can divide the array into two s1, s2

        We know s1 + s2 = total -> eq1

        We also know we need to assign positive and negative to array,
        so we assign +s1 and -s2

        From here we know 

        s1 - s2 = target -> eq 2

        From eq1 and eq2
        s1 + s2 = total
        s1 - s2 = target

        s1 = total - s2

        s1 - total + s1 = target

        2 * s1 = target + total

        s1 = (target + total) // 2


        """

        total = sum(nums)

        # We cannot divide the array into 2 halves
        if (target + total) % 2 != 0 or (target > total):
            return 0

        new_target = (total + target) // 2

        idx = n - 1

        return self.recursion(idx, new_target, nums)

    def recursion(self, idx, target, arr):
        # base case
        if idx < 0:
            if target == 0:
                return 1
            else:
                return 0
            
        # Logic
        if arr[idx] <= target:
            take = self.recursion(idx - 1, target - arr[idx], arr)
        else:
            take = 0
        
        no_take = self.recursion(idx - 1, target, arr)

        return take + no_take