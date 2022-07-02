'''
Heaps:
instead of storing all the value and sorting we can use heap. That will keep the top k value in heap.
Since python doesnot have max heap. To popout top k value we will append it along negative value.

1* Find the no of soldiers:  -->  While keeping track of their index.
To do this rather than performing leanier search, we can use binary search and get to know the no of soldiers.

2* Add them to heap:
While adding also check if heap len becomes equals to k. then pop the max no of soldiers

3* Return the index of the soldiers in the heap


# Time = O(rowlogcol * k)
# Space = O(k)



'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # heap: O(k) space and time
        heap = []
        
        #step 1: 
        for idx, row in enumerate(mat):
            no_of_soldiers = self.binarySearch(row)
            # print(no_of_soldiers)
            # create a entry with no_of_soldiers and idx
            # since min heap, add negative to convert to max heap
            entry = (-no_of_soldiers , -idx)
            
            
            #step 2:
            # check if heap is less then k
            # also check. If my current entry less than the first value in heap. Then we have to add it. Because we want smaller no of soldier.
            # since min queue we check if cur entry > heap[0]
            if len(heap) < k or entry > heap[0]:
                heapq.heappush(heap, entry)
                
            # pop the max no of soldier if len of heap same as k
            if len(heap) > k:
                heapq.heappop(heap)
                
        print(heap)
        
        #Step 3:
        return self.index_of_weakest_soldiers(heap)
        
        
    # log(row)    
    def binarySearch(self, row):
        left = 0
        right = len(row)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if row[mid] == 0:
                right = mid
            else:
                left = mid + 1
                
        return left
    
    
    def index_of_weakest_soldiers(self, heap):
        index_of_weakest_soldiers = []
        
        while heap:
            no_of_soldiers, idx = heapq.heappop(heap)
            index_of_weakest_soldiers.append(-idx)
            
        return index_of_weakest_soldiers[::-1]