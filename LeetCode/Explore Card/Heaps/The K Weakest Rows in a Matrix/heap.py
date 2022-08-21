# time: O(m log nk)
# space: O(k)

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        def binarySearch(arr):
            left = 0
            right = len(arr) - 1
            # print(arr)
            
            while left <= right:
                mid = left + (right - left) // 2
                # print(mid)
                
                if arr[mid] == 1:
                    left = mid + 1
                    # print("l",left)
                else:
                    right = mid - 1
                    # print("r",right)
            
            return right
        
        # find the strength
        heap = []
        
        for row, col in enumerate(mat):
            # print(row, col)
            soldiers = binarySearch(col)
            # print("sol",row, ": ", soldiers)
            entry = (-soldiers , -row) # -row because if there is a tie in index
            # print(entry)
            
            # if the heap is yet to be filled 
            # or if there are currently less soldiers push them in heap
            if len(heap) < k or entry > heap[0]:
                heapq.heappush(heap , entry)
            
            if len(heap) > k:
                heapq.heappop(heap)
                
            # print(heap)
            
        k_weakest = []
        
        while heap:
            _ , idx = heapq.heappop(heap)
            idx *= -1
            k_weakest.append(idx)
            
            
        return reversed(k_weakest) # since we need from smaller to larger
            
            
            
            