class Solution:
    def thirdDistinctLargest(self, arr):
        first = second = third = None

        for x in arr:
            if first is None or x > first:
                third = second
                second = first
                first = x
            elif x == first:
                continue

            elif second is None or x > second:
                third = second
                second = x
            elif x == second:
                continue
            
            elif third is None or x > third:
                third = x

        return third if third is not None else -1
