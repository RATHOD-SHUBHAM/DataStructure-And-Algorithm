'''
799. Champagne Tower
Medium

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.



Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)

 

Example 1:

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.
Example 2:

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
Example 3:

Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
 

Constraints:

0 <= poured <= 109
0 <= query_glass <= query_row < 100


'''

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        * dp = holds the number of glass in each row.
        * I will start from 1 because, If I start from 0. first value in dp will be [], but I want 1 glass in first row ie dp[1].
        
        * I will go up to query row + 2: 
        * because eg query_row = 5. 
        * then my range function should go from query_row + 1 = 6: ie 1,2,3,4,5. 
        * but Now according to index then my 
            row 0 will have 1 glass 
            1 = 2 glass, 
            2 = 3 glass, 
            3 = 4 glass,  
            row 4 = 5 glass and at, 
            row 5 it will give index out of bound.

        '''
        dp = [[0 for _ in range(row) ] for row in range (1, query_row + 2) ]
        # print(dp)
        
        dp[0][0] = poured
        # print(dp)
        
        # for every row until query row: index start from 0
        for i in range(query_row):
            # go throught every glass it has at that particular row
            for j in range(len(dp[i])):
                excess_liquid = (dp[i][j] - 1) / 2.0 # i want a float value
                # print("excess_liq: ",excess_liquid)
                
                # if there is excess liquid
                if excess_liquid > 0:
                    # divide it into 2 glass below it
                    dp[i+1][j] += excess_liquid
                    dp[i+1][j+1] += excess_liquid
                
        if dp[query_row][query_glass] < 1:
            return dp[query_row][query_glass]
        else:
            return 1 # sometimes there is a chance that particular glass has excess liquid. But lets not forget that max capacit of a glass is 1