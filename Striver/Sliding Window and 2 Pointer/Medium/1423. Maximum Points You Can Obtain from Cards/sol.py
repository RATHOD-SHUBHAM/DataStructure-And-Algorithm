'''
We can either pick k elements from the front or pick k elements from end, 
We can pick some elements from the front and some from back aswell.

We cannot pick elements from inbetween, the elements that are picked must be contineous.

'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        maxPoints = -math.inf

        # Pick all the elements from Front
        leftSum = 0
        for i in range(k):
            leftSum += cardPoints[i]
        
        maxPoints = max(maxPoints , leftSum)
        
        # Pick from front and back
        rightSum = 0
        right = n - 1
        for i in reversed(range(k)):
            leftSum -= cardPoints[i]
            rightSum += cardPoints[right]
            right -= 1

            cur_sum = leftSum + rightSum

            maxPoints = max(maxPoints , cur_sum)
        

        return maxPoints
    


#  -------------  Same Solution --------------

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        maxPoints = -math.inf

        # Pick all the elements from Front
        leftSum = sum(cardPoints[:k])
        maxPoints = max(maxPoints , leftSum)
        
        # Pick from front and back
        rightSum = 0
        right = n - 1
        for i in reversed(range(k)):
            leftSum -= cardPoints[i]
            rightSum += cardPoints[right]
            right -= 1

            cur_sum = leftSum + rightSum

            maxPoints = max(maxPoints , cur_sum)
        

        return maxPoints