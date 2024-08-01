class Solution:
    def thirdLargest(self,arr, n):
        # code here
        largest = -1
        
        for i in range(n):
            cur_ele = arr[i]
            
            if cur_ele > largest:
                largest = cur_ele
        
        second = -1
        for i in range(n):
            cur_ele = arr[i]
            
            if cur_ele < largest and cur_ele > second:
                second = cur_ele
        
        
        third = -1
        for i in range(n):
            cur_ele = arr[i]
            
            if cur_ele < second and cur_ele > third:
                third = cur_ele
        
        return third