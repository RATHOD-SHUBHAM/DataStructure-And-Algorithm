# Tc: O(n)
# Sc: O(1)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        total_candy = 1

        i = 1 # starting from index 1
        while i < n:

            # if ratings[i] == ratings[i-1]:
            #     total_candy += 1
            #     i += 1
            #     continue
            while i < n and ratings[i] == ratings[i-1]:
                total_candy += 1
                i += 1
            
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
