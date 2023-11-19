class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # print(self.heap)
        # print("\n")
        
        
        # make the heap len equal to k
        while len(self.heap) > self.k :
            heapq.heappop(self.heap)
            
        # print(self.heap)
        # print("\n")

    def add(self, val: int) -> int:
        heapq.heappush(self.heap , val)
        # print(self.heap)
        # print("\n")
        
        if len(self.heap) > self.k :
            heapq.heappop(self.heap)
        # print(self.heap)
        # print("\n")
        
        return self.heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)