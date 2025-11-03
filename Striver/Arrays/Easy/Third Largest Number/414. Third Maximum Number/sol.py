class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)

        first = second = third = None

        for x in nums:
            if first is None or x > first:
                third = second
                second = first
                first = x
            # Avoid Duplicates
            elif x == first:
                continue

            elif second is None or x > second:
                third = second
                second = x
            # Avoid Duplicates
            elif x == second:
                continue
            
            elif third is None or x > third:
                third = x
        

        return third if third is not None else first