# we perform binary search on range of number and not on index
class Solution:
    def CountLessThanMid(self, mat , mid , smallest, largest):
        count = 0 # keep track of how many number are lesser than mid
        mat_len = len(mat)
        
        # starting from last row
        row = mat_len - 1
        col = 0
        
        while row >= 0 and col < mat_len:
            # if the cur val is greater than mid value
            if mat[row][col] > mid:
                # next largest element to mid
                largest = min(largest , mat[row][col])
                # all the ele to the right will be greater than cur row. so move top
                row -= 1
                
            else:
                # next smallest value than mid
                smallest = max(smallest, mat[row][col])
                # all the value above will be less. so move to right
                col += 1
                count += row + 1 #all the value until that row will be smaller so count them
                # since zero index we add + 1
                
        return smallest, largest, count
    
    
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]
        
        while left < right:
            mid = left + (right - left) // 2
            # print("mid: ",mid)
            
            smallest, largest = (matrix[0][0] , matrix[-1][-1])
            
            # smallerst number before mid
            # larger number after mid
            smaller, larger, count = self.CountLessThanMid(matrix, mid, smallest, largest)
            # print("count: ",count)
            # print("smaller: ",smaller)
            # print("larger: ",larger)
            # now i got the value immediately smaller than mid
            # value that is immediatlely larger than mid
            # and numberr of elment smaller than mid
            if count == k:
                return smaller # because that will be the kth smallest element
            elif count < k:
                left = larger
            else:
                right = smaller
                
        return right # or return left as there is only one element
        