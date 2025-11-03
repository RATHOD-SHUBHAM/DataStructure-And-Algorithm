class Solution:
    def thirdLargest(self,arr):
        # code here
        n = len(arr)
        
        first = second = third = float("-inf")
        
        for x in arr:
            # Largest Element
            if x > first:
                third = second
                second = first
                first = x
            
            # Second Largest
            elif x >= second:
                third = second
                second = x
            
            # Third Largest 
            elif x > third: # This can also be >=
                third = x
        
        return third if third != float("-inf") else -1
                
                
