'''
Figure out the number of odd places and number of even places:
    Given n:
        no of odd places = n // 2
        no of even places = n // 2 + n % 2

- Odd place can have 4 values,
    so 4 ^ no of odd places

- Even place can have 5 values
    so 5 ^ no of even places

eg : n = 5
0 1 2 3 4
    0 2 4 -> Even = 3
    1 3 -> Odd = 2

so total val = (5 ^ 3) * (4 ^ 2)
    5 even value ("0", "2", "4", "6", "8") for 3 place
    4 odd value (2, 3, 5, or 7) for 2 places
'''

# Memory Error

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10 ** 9) + 7

        # get the odd place and even place
        no_of_odd_places = n // 2
        no_of_even_place = (n // 2) + (n % 2)

        # Compute Place holder value
        odd_res = self.power(4 , no_of_odd_places) 
        even_res = self.power(5 , no_of_even_place)

        return (odd_res * even_res) % MOD

    
    def power(self, x, n):
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        if n % 2 == 0:
            result = self.power(x , n // 2)
            result = result * result
            
            return result
        
        elif n % 2 == 1:
            result = self.power(x , n // 2)
            result = result * result

            result = x * result
            return result