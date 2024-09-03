'''
If k is less than sum, we will reach zero within the first cycle. 
If k is greater than sum, after the first cycle, k will be reduced to k - sum, 
and after subsequent cycles, it will be reduced further. 

This process continues until k becomes less than sum, 
which is equivalent to computing k % sum
'''

# Tc: O(n) | SC: O(1)

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        chalk_sum = sum(chalk)

        '''
        k value:  k // sum = How many complete cycle can be done,
                    k % sum = what will be remaining value after x complete value. 
        '''
        k = k % chalk_sum

        # print(k)

        for i in range(n):
            cur_chalk = chalk[i]

            if k < cur_chalk:
                # print(k)
                return i
            
            k -= cur_chalk
        
        return 0