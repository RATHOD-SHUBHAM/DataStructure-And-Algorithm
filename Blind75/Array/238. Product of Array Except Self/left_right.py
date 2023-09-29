# Tc Sc: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Running Product: Product of all element except self

        left = [1] * n
        right = [1] * n

        # Left running product: Left -> Right
        running_prod = 1
        for i in range(n):
            left[i] = running_prod
            # Calculate the running prod
            running_prod *= nums[i]

        # Right running prod: Right -> Left
        running_prod = 1
        for i in reversed(range(n)):
            right[i] = running_prod
            # Calculate the runnning prod
            running_prod *= nums[i]

        # Compute Final Running Prod
        running_p = [1] * n
        for i in range(n):
            running_p[i] = left[i] * right[i]
        
        return running_p