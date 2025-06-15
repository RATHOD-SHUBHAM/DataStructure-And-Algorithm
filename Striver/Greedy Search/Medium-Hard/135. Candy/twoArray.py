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
        left_candies = [1] * n

        for i in range(n):
            if i-1 >= 0:
                if ratings[i-1] < ratings[i]:
                    left_candies[i] = left_candies[i-1] + 1
        
        # Firstly, we give 1 candy to each student.
        right_candies = [1] * n

        for i in reversed(range(n)):
            if i+1 < n:
                if ratings[i+1] < ratings[i]:
                    right_candies[i] = right_candies[i+1] + 1
        
        """
        Now, for the i'th student in the array, we need to give max(left2right[i], right2left[i]) to them, 
        in order to satisfy both the left and the right neighbor relationship. 
        """
        min_candies = 0
        for i in range(n):
            min_candies += max(left_candies[i], right_candies[i])

        return min_candies