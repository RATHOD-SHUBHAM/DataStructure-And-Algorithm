class Solution:
    def thirdLargest(self,arr, n):
        # code here
        largest = -1
        second = -1
        third = -1
        
        for i in range(n):
            cur_ele = arr[i]
            
            if cur_ele > largest:
                third = second
                second = largest
                largest = cur_ele
            
            elif cur_ele < largest and cur_ele > second:
                third = second
                second = cur_ele
            
            elif cur_ele < second and cur_ele > third:
                third = cur_ele
        
        
        return third