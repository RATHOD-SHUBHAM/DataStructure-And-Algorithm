# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
import heapq
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.lower = [] # max heap
        self.upper = [] # min heap
        self.median = None

        heapq.heapify(self.lower)
        heapq.heapify(self.upper)

        
    def insert(self, number):
        # Write your code here.
        if len(self.lower) == 0 or number < self.peek(self.lower , True):
            num = -1 * number # adjust it as max heap
            heapq.heappush(self.lower, num)
        else:
            heapq.heappush(self.upper, number)

        self.rebalanceHeap()

        self.calMedian()

    def getMedian(self):
        return self.median

    def peek(self, heap, isMaxHeap):
        if len(heap) == 0:
            return 

        if isMaxHeap:
            top_of_heap = heapq.heappop(heap)
            #adjust according to max heap
            adjsuted_top_of_heap = top_of_heap * -1
            #push back the element into heap
            heapq.heappush(heap, top_of_heap)
            return adjsuted_top_of_heap
        else:
            top_of_heap = heapq.heappop(heap)
            heapq.heappush(heap, top_of_heap)
            return top_of_heap

    def rebalanceHeap(self):
        if len(self.lower) - len(self.upper) == 2:
            # remove from top of max heap and push into min heap
            top_of_max_heap = heapq.heappop(self.lower)
            adjusted_top_of_max_heap = -1 * top_of_max_heap
            heapq.heappush(self.upper, adjusted_top_of_max_heap)
        elif len(self.upper) - len(self.lower) == 2:
            top_of_min_heap = heapq.heappop(self.upper)
            # adjust it as per max heap
            adjusted_top_of_min_heap = -1 * top_of_min_heap
            heapq.heappush(self.lower, adjusted_top_of_min_heap)
        else:
            pass

    def calMedian(self):
        if len(self.lower) == len(self.upper):
            self.median = (self.peek(self.lower, True) + self.peek(self.upper, False)) / 2
        elif len(self.lower) > len(self.upper): 
            self.median = self.peek(self.lower, True)
        else:
            self.median = self.peek(self.upper, False)
            