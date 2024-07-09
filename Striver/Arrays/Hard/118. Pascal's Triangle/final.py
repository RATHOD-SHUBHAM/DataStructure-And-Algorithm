class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_op = [[1]] # BASE CASE - by default we should have [1]

        for i in range(1, numRows):
            arr = final_op[-1]
            cur_list = []


            for j in range(1, len(arr)):
                cur_sum = arr[j-1] + arr[j] # current number is always sum of current and previous index
                cur_list.append(cur_sum)
            
            new_list = [1] + cur_list + [1]

            final_op.append(new_list)
        
        return final_op