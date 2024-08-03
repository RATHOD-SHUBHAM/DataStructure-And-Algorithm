class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # count no of inflation/break points
        count = 0

        for i in range(n):
            # Compare every element to its previous element - also compare the last element to the first element.
            if nums[(i-1) % n] > nums[i]:        
                count += 1

            if count > 1:
                # if break point greater than one, array cant be rotated
                return False
        
        return True