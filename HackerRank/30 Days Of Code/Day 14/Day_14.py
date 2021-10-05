# todo:  brute force approach  O(n^2)

"""
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        for i in range(0, len(self.__elements)):
            for j in range(i + 1, len(self.__elements)):
                diff = abs(self.__elements[i] - self.__elements[j])
                self.maximumDifference = max(self.maximumDifference, diff)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

"""


#todo : reducing to O(n)
# max and min - Time Complexity is O(n) and Space Complexity is O(1)

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        self.maximumDifference = max(self.__elements)-min(self.__elements)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)