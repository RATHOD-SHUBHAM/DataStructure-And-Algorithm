# -------------------------- Two Array Greedy --------------------------

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
        left_candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_candies[i] = left_candies[i-1] + 1
        
        # assign candies from right to left
        right_candies = [1] * n
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                right_candies[i] = right_candies[i+1] + 1
        
        # We need max(left, right), in order to satisfy both the left and the right neighbor relationship. 
        candies = [1] * n
        for i in range(n):
            candies[i] = max(left_candies[i], right_candies[i])
        
        # print(candies)
        return sum(candies)


# -------------------------- Single Array Greedy --------------------------

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

# --------------------------  Peak and Down Valley --------------------------
# Tc: O(n)
# Sc: O(1)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        total_candy = 1

        i = 1 # starting from index 1
        while i < n:

            if ratings[i] == ratings[i-1]:
                total_candy += 1
                i += 1
                continue
            
            # We reset the peak and down to 1
            peak = 1
            down = 1 # for the previous idx [i-1]

            # Moving Up
            while i < n and ratings[i] > ratings[i-1]:
                
                # We increase peak first because, we need more candies than previous one
                peak += 1
                total_candy += peak
                i += 1

            
            # Moving Down
            while i < n and ratings[i] < ratings[i-1]:
                # Moving down
                # We calculate sum first becasue the next neighbor should get more candies than current
                total_candy += down
                down += 1
                i += 1
            
            # Peak element should always be greates
            # Each element in the descending sequence must have 1 fewer candy than the previous element, starting from the peak
            if down > peak:
                # Adjust the peak value
                total_candy += down - peak
        
        return total_candy
