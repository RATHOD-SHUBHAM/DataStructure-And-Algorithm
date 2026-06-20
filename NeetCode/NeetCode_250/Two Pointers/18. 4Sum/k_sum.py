class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sorting is essential: enables pruning, duplicate-skipping,
                     # and two-pointer technique in the base case
        return self.kSum(nums, target, 0, 4)

    def kSum(self, nums, target, start, k):
        """
        Generic K-Sum solver.
        Finds all unique k-tuples (using elements from index >= start)
        that sum to `target`, in a sorted `nums` array.

        Recursion idea:
            kSum(k) fixes one number, then delegates to kSum(k-1)
            to find the remaining (k-1) numbers that sum to (target - fixed number).
            Base case k == 2 is solved directly with two-pointer (twoSum).
        """
        res = []
        n = len(nums)

        # ---- Pruning / impossible-case checks ----
        # 1) Not enough elements left to pick from.
        # 2) Smallest possible sum (k copies of the smallest remaining value)
        #    already exceeds target -> no valid combination possible.
        # 3) Largest possible sum (k copies of the largest value in array)
        #    is still less than target -> no valid combination possible.
        if start == n or nums[start] * k > target or nums[-1] * k < target:
            return res

        # ---- Base case: 2 numbers left, solve with two-pointer ----
        if k == 2:
            return self.twoSum(nums, target, start)

        # ---- General case: pick one number, recurse for the rest ----
        # Loop bound `n - k + 1` ensures there are always enough elements
        # remaining after index i to form the rest of the k-tuple.
        for i in range(start, n - k + 1):

            # Skip duplicate values at this position to avoid duplicate tuples.
            # When i == start → this is the first number we're trying at this position. There's nothing to compare against (within this call), so we never skip it.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If nums[i] alone (repeated k times) already exceeds target,
            # every element after it (sorted, so >= nums[i]) will too.
            # No point continuing the loop -> break entirely.
            if nums[i] * k > target:
                break

            # If nums[i] plus the maximum possible sum of the remaining
            # (k-1) numbers (all taking the largest value nums[-1])
            # is still less than target, nums[i] is too small to work.
            # A larger nums[i] might still work, so just skip (not break).
            if nums[i] + nums[-1] * (k - 1) < target:
                continue

            # Fix nums[i] as one number of the tuple, recursively find
            # the remaining (k-1) numbers (starting after i) that sum
            # to (target - nums[i]).
            for sub in self.kSum(nums, target - nums[i], i + 1, k - 1):
                res.append([nums[i]] + sub)  # prepend the fixed number

        return res

    def twoSum(self, nums, target, start):
        """
        Two-pointer solution for finding all unique pairs in nums[start:]
        that sum to target. Requires nums to be sorted.
        """
        res = []
        j, k = start, len(nums) - 1

        while j < k:
            s = nums[j] + nums[k]

            if s == target:
                # Found a valid pair
                res.append([nums[j], nums[k]])
                j += 1
                k -= 1

                # Skip duplicate values on the left pointer side
                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                # Skip duplicate values on the right pointer side
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

            elif s < target:
                # Sum too small -> move left pointer right to increase sum
                j += 1
            else:
                # Sum too large -> move right pointer left to decrease sum
                k -= 1

        return res
    

# ========================== Clean Solution ==========================

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 0, 4)

    def kSum(self, nums, target, start, k):
        res = []
        n = len(nums)

        if start == n or nums[start] * k > target or nums[-1] * k < target:
            return res

        if k == 2:
            return self.twoSum(nums, target, start)

        for i in range(start, n - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue

            if nums[i] * k > target:
                break

            if nums[i] + nums[-1] * (k - 1) < target:
                continue

            for sub in self.kSum(nums, target - nums[i], i + 1, k - 1):
                res.append([nums[i]] + sub)
        
        return res

    def twoSum(self, nums, target, start):
        res = []
        j, k = start, len(nums) - 1
        while j < k:
            s = nums[j] + nums[k]
            if s == target:
                res.append([nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif s < target:
                j += 1
            else:
                k -= 1
        return res
        