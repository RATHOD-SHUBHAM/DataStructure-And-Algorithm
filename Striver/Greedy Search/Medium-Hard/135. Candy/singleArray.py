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

        # We give 1 candy to each student.
        # assign candies from left to right
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # assign candies from right to left
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                cur_candy = candies[i+1] + 1
                candies[i] = max(candies[i] , cur_candy)
        
        # print(candies)
        return sum(candies)
