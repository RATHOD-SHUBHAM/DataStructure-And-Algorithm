# Tc: O(n)
# Sc: O(n)

"""
Consider Examples: 
arr: [1,2,87,87,87,2,1]
arr: [1,3,4,5,2]

# Runnign Sum: Left Right Array
    * The left2right array is used to store the number of candies required by the current student taking care of the distribution relative to the left neighbors only. i.e. Assuming the distribution rule is: The student with a higher rating than their left neighbor should always get more candies than its left neighbor. 
    * Similarly, the right2left array is used to store the number of candies required by the current student taking care of the distribution relative to the right neighbors only.
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        # Firstly, we give 1 candy to each student.
        candies = [1] * n

        for i in range(n):
            if i-1 >= 0:
                if ratings[i-1] < ratings[i]:
                    candies[i] = candies[i-1] + 1
        
        """
        This time we need to update candies[i] only if candies[i] <= candies[i + 1]. 
        This happens because this time we've already altered the candies array during the forward traversal and thus candies[i] isn't necessarily less than or equal to candies[i + 1].
        """
        for i in reversed(range(n)):
            if i + 1 < n:
                if ratings[i+1] < ratings[i]:
                    candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)